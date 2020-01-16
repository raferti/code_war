"""

For this exercise you will be strengthening your page-fu mastery. You will
complete the PaginationHelper class, which is a utility class helpful for
querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating
how many items will be allowed per each page. The types of values contained
within the collection/array are not relevant.

The following are some examples of how this class is used:

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count # should == 2
helper.item_count # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_ndex takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

"""


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self._count_item = len(collection)

    def item_count(self):
        """Возвращает количество элементов во всей коллекции"""

        return self._count_item

    def page_count(self):
        """Возвращает количество страниц"""

        page_count = ((self._count_item - 1) / self.items_per_page) + 1
        return int(page_count)

    def page_item_count(self, page_index):
        """Возвращает количество элементов на текущей странице. page_index
        основан на нуле этот метод должен возвращать -1 для значений
        page_index, которые находятся вне диапазона
        """

        if self.page_count() == page_index + 1:
            return self._count_item % self.items_per_page
        elif page_index < 0 or page_index > self.page_count()-1:
            return -1
        else:
            return self.items_per_page

    def page_index(self, item_index):
        """Определяет, на какой странице находится элемент. Нулевые индексы.
        этот метод должен возвращать -1 для значений item_index, которые
        находятся вне диапазона
        """

        if (item_index >= 0) and (item_index < self._count_item):
            return int(((item_index - 1) / self.items_per_page))
        else:
            return -1


# Testing
# collections = range(1, 10)
# helper = PaginationHelper(collections, 4)

