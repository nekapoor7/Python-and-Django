"""Do sum in a nested list of a given list"""

#l2 = [1,2,[2,2],[3,3]]


class Sum:
    def add(self, nlist):
        total = 0
        for element in nlist:
            if type(element) == list:
                total += self.add(element)
            else:
                total += element
        return total


def main():
    nested_list = [1,2,[2,2],[3,3]]
    obj = Sum()
    total = obj.add(nested_list)
    print("Total Sum:", total)


if __name__ == "__main__":
    main()