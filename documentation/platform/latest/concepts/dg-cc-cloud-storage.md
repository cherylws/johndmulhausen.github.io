---
title: Cloud Storage
---
Seamlessly save, synchronize, and load data between devices and installs using our Cloud Storage service.

Note: Cloud Storage is only available for Rift apps.Cloud Storage is designed to support the following use-cases in Rift apps:

1. Save progress between installs. Users are able to uninstall and re-install without losing their saved data.
2. Share progress between devices. Users can sync data between user devices.
3. Disaster recovery. User data can be restored if devices are lost or damaged, or if the local data is corrupted.
**Storage Formats**

The Cloud Storage service uses buckets (directories) and blobs (files), indexed by a key (file name), to store data. The number of blobs stored per bucket can not exceed 10,000. However, apps should use a smaller limit for the number of blobs, as the resources required to process a large number of keys may impact the user’s experience.

Direct file storage is not supported.

Note: The Cloud Storage service does not retain old versions of data. An app that needs old save files preserved should store them using a bucket/key backup strategy. For example, creating buckets saved\_games\_prior1 and saved\_games\_prior2 would allow to you store 2 old save files in addition to the latest save. ## Data Storage Structure

Cloud Storage is divided into buckets (directories) of data that are configured in the Developer Center, under the [Cloud Storage](https://dashboard.oculus.com/app/cloud-storage) tab. Apps may define more than one bucket for multiple save types or data. 

For example, when creating a new save you would call ovr\_CloudStorage\_Save(bucket\_name, key, data\_pointer, data\_size, counter, extra\_data). More details can be found in the ovr\_CloudStorage\_Save reference.

* bucket\_name - The name defined in the Developer Center.
* key - The unique index for the blob. Total size cannot exceed 512 bytes.
* data\_pointer - The pointer to the data blob in your app.
* data\_size - The size, in bytes, of the data blob.
* counter - The counter is an incremented uint64 metadata. The value is optional unless the Highest Counter conflict resolution policy is specified.
* extra\_data - Any extra, optional, metadata. Total size cannot exceed 512 bytes as a unsigned 64bit integer data. 
## Creating Buckets

In the [Cloud Storage](https://dashboard.oculus.com/app/cloud-storage) tab of the Developer Center click the **Create Cloud Storage Bucket** button and enter the information about the bucket that you would like to create. The bucket name is case-sensitive, the name you define in the Dashboard must exactly match the bucket\_name you reference in your code. 

Information about conflict management strategies can be found below in the *Managing Conflicts* section below.

## Integrating Cloud Storage - Native & Unity

Once you've defined the Cloud Storage buckets, you can integrate the service into your game. When calling the methods listed below you'll reference the bucket\_name you created for the bucket. 

The following is the typical Cloud Storage lifecycle:

1. Retrieve a list of the entries in each Cloud Storage bucket you've defined by calling ovr\_CloudStorage\_LoadBucketMetadata(). Perform any conflict resolution required if the data retrieved is not in sync with the local data. Information about how to resolve conflicts can be found later in this guide. 
2. Once the metadata has been loaded and you've determined which save data you need to load, call ovr\_CloudStorage\_Load(), with the data key, to load the data. You can now launch your game using the game state data you loaded. 
3. During gameplay and at the prompt of the user, save the game state data by calling ovr\_CloudStorage\_Save() with the data blob. We recommend triggering saves once a minute, at most, and when prompted to prevent runaway game saves.
4. When quitting the game, make sure to reconcile local and cloud saves ensuring that the latest data is saved to the Cloud Storage service. 
Note: We recommend that you review the sample app described below for a detailed walk-through of how you may implement the Cloud Storage service. The following SDK methods can be called from your client app. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.").

* **Save a blob:**

Native - ovr\_CloudStorage\_Save()

Unity - Platform.CloudStorage.Save()

This call sends the blob data to the locally running Oculus process and will not trigger network calls. Network synchronization happens when the App is no longer running. Total size for a blob can not exceed 10Mb.

Note:ovr\_CloudStorage\_Save passes a pointer to your data in an async call. You need to maintain the save data until you receive a ovrMessage\_CloudStorage\_Save message indicating that the save was successful. If the data is destroyed or modified prior to receiving that message the data will not be saved.
* **Load a blob:**

Native - ovr\_CloudStorage\_Load()

Unity - Platform.CloudStorage.Load()

If the bucket is configured for manual conflict resolution and a conflict exists between the local and remote versions, the load call will return an error. The process to resolve conflicts is discussed below. Loading a blob will not initiate a network call.


* **Delete a blob:**

Native - ovr\_CloudStorage\_Delete()

Unity - Platform.CloudStorage.Delete()

This will delete both the cloud and local copies of the blob. You may write new data to a deleted blob without waiting for synchronization.


* **Find a blob:**

You may want to retrieve some information about the available blobs to determine which one to load. The following methods allow you to retrieve the metadata for one or all saved data blobs.


	+ **Retrieve blob metadata for all blobs:**
	
	Native - ovr\_CloudStorage\_LoadBucketMetadata(bucket\_name)
	
	Unity - Platform.CloudStorage.LoadBucketMetadata(bucket\_name)
	
	
	+ **Retrieve blob metadata for a specific blob:**
	
	Native - ovr\_CloudStorage\_LoadMetadata(bucket\_name, key)
	
	Unity - Platform.CloudStorage.LoadMetadata(bucket\_name, key)
	
	
	
**Blob Metadata**

Both of the metadata requests will return results in the same format. Use the metadata information to determine which save you want to load.

The response payload will be in the following format:

uint32 data\_size = ovr\_CloudStorageMetadata\_getDataSize(metadataHandle) uint64 saved\_time = ovr\_CloudStorageMetadata\_getSaveTime(metadataHandle) int64 counter = ovr\_CloudStorageMetadata\_getCounter(metadataHandle) const char* extra\_data = ovr\_CloudStorageMetadata\_getExtraData(metadataHandle) ovrCloudStorageVersionHandle handle = ovr\_CloudStorageMetadata\_getHandle(metadataHandle) ovrCloudStorageDataStatus status = ovr\_CloudStorageMetadata\_getStatus(metadataHandle)* data\_size - The size, in bytes, of the stored data blob.
* saved\_time - the UTC time, in seconds, since the UNIX epoch when the blob was locally saved. This is the time as recorded on the local device so includes local clock skew.
* counter - The value specified when saved, else zero.
* extra\_data - the value specified when saved, else null.
* handle - used for manual conflict resolution (see below).
* status - enum describing the state of the blob. This state as determined by the most recent network update. The following states are possible: 
	+ ovrCloudStorageDataStatus\_InSync - the local and remote versions are in-sync.
	+ ovrCloudStorageDataStatus\_NeedsDownload - a newer version exists in the cloud but hasn't yet downloaded. 
	+ ovrCloudStorageDataStatus\_NeedsUpload - the local version is newer and needs to be uploaded. 
	+ ovrCloudStorageDataStatus\_InConflict - the local and remote version have a conflict that must be manually resolved. Only occurs for buckets set to manual conflict resolution.
	
## Integrating Cloud Storage - Unreal

Once you've defined the Cloud Storage buckets, you can integrate the service into your game. Complete information for this API can be found in Epic's [IOnlineUserCloud](https://docs.unrealengine.com/latest/INT/API/Plugins/OnlineSubsystem/Interfaces/IOnlineUserCloud/) documentation.

In your pap’s DefaultEngine.ini file, add the following.

[OnlineSubsystem] DefaultUserCloudBucket=<YOURBUCKETNAME>Where <YOURBUCKETNAME> is the bucket name that you defined on the Dashboard.

Then, to integrate Cloud Storage:

* **Find a blob/file:**

First call - EnumerateUserFiles()

Then call - GetUserFileList()

Retrieve the list of saved files that are available to load. The EnumerateUserFiles() function may require numerous round trips to get a complete list of save data. 


* **Load a blob/file:**

First call - ReadUserFile()

Then call - GetFileContents()

Retrieve and load the identified save file. 


* **Save a blob:**

Unreal - WriteUserFile()

This call sends the blob data to the locally running Oculus process and will not trigger network calls. Network synchronization happens when the App is no longer running. Total size for a blob can not exceed 10Mb.

Note:WriteUserFile() passes a pointer to your data in an sync call. You need to maintain the save data until you receive an indication that the save was successful. If the data is destroyed or modified prior to receiving that message the data will not be saved. You may call CancelWriteUserFile() to cancel the write operation.
* **Clear local saves:**

Unreal - ClearFiles()

Unreal - ClearFile()

These methods will clear either a single identified, or all locally saved files.


* **Delete a blob:**

Unreal - DeleteUserFile()

This will delete both the cloud and local copies of the blob. You may write new data to a deleted blob without waiting for synchronization.


## Managing Conflicts

The Cloud Storage service supports synchronizing data between multiple devices and platforms. This requires a conflict resolution strategy to handle situations where multiple devices may upload blobs to the same key. This situation is common on mobile devices but can occur between PCs as well. The following resolution strategies are available:

**Latest TimeWarp**

Resolving the conflict by using the latest timestamp is the least complex resolution. It configures the bucket to prefer the blob that has the timestamp recorded most recently by the local device. A timestamp is recorded at the time the call to ovr\_CloudStorage\_Save() is made. Client blobs with timestamps earlier than the remotely stored version are discarded.

**Highest Counter**

Buckets configured with the highest counter method will prefer blobs with the highest value set in the counter field. This method could be used if you wanted to preserve the blob with the highest score. Blobs stored with the same counter value as a remote version will attempt to be stored. However, multiple devices doing this represent a race-condition where either device may win.

**Manual** - Only available in Native and Unity apps.

You may also choose to handle conflict resolution entirely in your app. When an app saves a new local blob to a specific key that's in state ovrCloudStorageDataStatus\_InConflict, the blob will not be uploaded until the app resolves the conflict. Conflict resolution can be done at any time but it's best done during App startup and shutdown. The need for manual conflict resolution can be detected by checking the metadata status, or by reviewing the save message response.

ovrCloudStorageUpdateResponseHandle response = ovr\_Message\_GetCloudStorageUpdateResponse(save\_message) ovrCloudStorageUpdateStatus status = ovr\_CloudStorageUpdateResponse\_GetStatus(response)) if (status == ovrCloudStorageUpdateStatus\_ManualMergeRequired) { // perform manual merge... }The first step to resolving is to load the metadata for the conflicting blobs:

ovr\_CloudStorage\_LoadConflictMetadata(bucket, key)This is an asynchronous call and the response message is parsed to get the metadata:

ovrCloudStorageConflictMetadataHandle response = ovr\_Message\_GetCloudStorageConflictMetadata(message) ovrCloudStorageMetadataHandle local\_metadata = ovr\_CloudStorageConflictMetadata\_GetLocal(response) ovrCloudStorageMetadataHandle remote\_metadata = ovr\_CloudStorageConflictMetadata\_GetRemote(response)* **Resolving based on metadata**

If the metadata for the blob contains enough information to resolve the conflict, then the next step is to call:

ovr\_CloudStorage\_ResolveKeepRemote(bucket\_name, key, remote\_handle)to choose the remote blob, or:

ovr\_CloudStorage\_ResolveKeepLocal(bucket\_name, key, remote\_handle)to choose the local blob. The handle from the remote blob's metadata is passed in to prevent data loss in the instance that a new remote blob appears during conflict resolution.


* **Resolving by inspecting data**

If you need to inspect the data blobs to determine which to keep, they can be loaded using the handle from the metadata:

ovr\_CloudStorage\_LoadHandle(handle)This works for both the local and remote handles. If the remote blob has not been cached locally, requesting the remote will initiate a network call to fetch any remaining data.


* **Resolving by merging the remote and local data**

If the app needs to merge the saved blobs, they can be loaded as described above, then the app can save a new local version and resolve by choosing that:

ovr\_CloudStorage\_Save(bucket\_name, key, merged\_data\_pointer, merged\_data\_size, counter, extra\_data) ovr\_CloudStorage\_ResolveKeepLocal(bucket\_name, key, remote\_handle)
## Example Implementation

The CloudStorageSample Unity app provided in the Platform SDK [download](/downloads/) demonstrates using the Cloud Storage service to save multiple records and perform conflict resolution. Please see the [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) page for more information about the apps that are available.

