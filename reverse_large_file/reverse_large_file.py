
# read 10 bytes per read
CHUNK_SIZE = 10

# assume the following is given
class FileObj:
    def open(self):
        """ 
        Open the file with the name filename.
        """
        pass

    def close(self):
        """ 
        Close the file. 
        """
        pass

    def read(self, buff, offset, num_bytes) :
        """ 
        buff: bytes, offset: int, num_bytes: int
        Read num_bytes bytes into buff from the file, starting at offset.
        """
        pass

    def write(self, buff, offset, num_bytes):
        """ 
        buff: bytes, offset: int, num_bytes: int
        Write num_bytes bytes from buff into the file, starting at offset. bytes should
        be a bytearray containing the bytes to write.
        """         
        pass 


def f_open(filename):
    """
    Open the file and returns a FileObj.
    """
    fp = FileObj()
    fp.open(filename)
    return fp


def reverse_large_file(filename):

    print(f"Open a file: { filename }")
    fp = f_open(filename)

    # file pointer set to the end of the file
    # second arg: start:0, current:1, end:2
    fp.seek(0, 2) 
    
    # size in bytes
    size = fp.tell()

    print(f"The file lenght in bytes is { size }")
    print(f"Read from the file { CHUNK_SIZE } bytes from both end at a time.")

    left_ptr, right_ptr = 0, size
    while True:
        if right_ptr-CHUNK_SIZE < left_ptr+CHUNK_SIZE:
            last_chunk = (right_ptr-left_ptr) // 2
            helper(fp, left_ptr, right_ptr, last_chunk)
            break
        helper(fp, left_ptr, right_ptr, CHUNK_SIZE)
        left_ptr += CHUNK_SIZE
        right_ptr -= CHUNK_SIZE
	
    print(f"Done reversing the file: { filename }")
    fp.close()


def helper(fp, left_ptr, right_ptr, chunk):
    left_chunk, right_chunk = "", ""
    fp.read(left_chunk, left_ptr, chunk)
    fp.read(right_chunk, right_ptr, chunk)
    left_chunk.reverse()		
    right_chunk.reverse()
    fp.write(right_chunk, left_ptr, chunk)
    fp.write(left_chunk, right_ptr, chunk)


def main():
    reverse_large_file("fileinput.txt")

if __name__ == "__main__":
    main()