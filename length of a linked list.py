def get_length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count +=1
            cur_node = cur_node.next

        return count

