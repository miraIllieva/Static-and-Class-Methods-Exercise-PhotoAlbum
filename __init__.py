from math import ceil


class PhotoAlbum:
    PAGE_SIZE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        album_pages = ceil(photos_count / cls.PAGE_SIZE)
        return cls(album_pages)

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"

        return "No more free slots"  # Fixed indentation

    def display(self):
        res = []
        res.append('-' * 11)
        for page in self.photos:
            res.append(' '.join('[]' for _ in page).ljust(PhotoAlbum.PAGE_SIZE * 3))  # Fixed formatting
            res.append('-' * 11)
        return '\n'.join(res)


# Testing the class
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
