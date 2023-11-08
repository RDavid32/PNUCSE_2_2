class DiskManger:
    def __init__(self, disk_size):
        self.disk_size = disk_size
        self.empty_disk_size = disk_size
        self.disk_name = []
        self.disk = [0, disk_size]

    def write_file(self, file_name, file_size):
        def insert_data(q, left, check_size):
            self.disk.insert(left + 1, self.disk[left] + check_size)
            self.disk.insert(left + 1, self.disk[left])
            self.disk_name.insert(q, file_name)

        if file_size > self.empty_disk_size:
            print("diskfull")
        elif file_name in self.disk_name:
            print("error")
        else:
            self.empty_disk_size -= file_size

            for q in range(len(self.disk_name) + 1):
                left, right = q * 2, q * 2 + 1
                if self.disk[right] - self.disk[left] >= file_size:
                    insert_data(q, left, file_size)
                    return

            check = file_size
            count = 0
            for q in range(len(self.disk_name)):
                left, right = q * 2 + count, q * 2 + 1 + count
                if space := self.disk[right] - self.disk[left]:
                    if space < check:
                        insert_data(q+count//2, left, space)
                        check -= space
                        count += 2
                    else:
                        insert_data(q+count//2, left, check)
                        return
            
            insert_data(q+count//2+1, q * 2 + count+2, check)


    def delete_file(self, disk_name):
        if disk_name in self.disk_name:
            for _ in range(self.disk_name.count(disk_name)):
                index = self.disk_name.index(disk_name)
                del self.disk_name[index]
                self.empty_disk_size += self.disk[index * 2 + 2] - self.disk[index * 2 + 1]
                del self.disk[index * 2 + 1 : index * 2 + 3]
        else:
            print("error")

    def show_disk(self, disk_name):
        if disk_name in self.disk_name:
            print(*[self.disk[i * 2 + 1] for i, value in enumerate(self.disk_name) if value == disk_name])
        else:
            print("error")

    def compact_disk(self):
        check = 0
        count = 0
        for q in range(0, len(self.disk) - 1, 2):
            self.disk[q] -= check
            self.disk[q + 1] -= check
            if space := self.disk[q + 1] - self.disk[q]:
                self.disk[q + 1] -= space
                check += space
        self.disk[-1] = self.disk_size
        
        for q in range(len(self.disk_name) - 1):
            check = q - count
            if self.disk_name[check] == self.disk_name[check + 1]:
                del self.disk_name[check]
                del self.disk[(check + 1) * 2: (check + 1) * 2 + 2]
                count += 1

v = int(input())
disk = DiskManger(v)
while True:
    print(disk.disk)
    print(disk.disk_name)
    command, *name = input().split()
    if command == "write":      disk.write_file(name[0],int(name[1]))
    elif command == "delete":   disk.delete_file(name[0])
    elif command == "show":     disk.show_disk(name[0])
    elif command == "compact":  disk.compact_disk()
    else:  break