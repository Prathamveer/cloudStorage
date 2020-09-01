import dropbox

class TransferData:
    def __init__(self,acToken):
        self.acToken=acToken
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.acToken)
        print(file_from)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
def main():
    accessToken="hlgwiXFNwooAAAAAAAAAAUMMMsBlrLIlMaym8sSCyBD7sllEwdkPO6TIMbP9vkm3"
    transferData=TransferData(accessToken)
    file_from=input("Enter the file path from which to transfer:")
    file_to=input("Enter the path to upload to the dropbox:")
    transferData.upload_file(file_from,file_to)
    print("File has been transferred.")

main()