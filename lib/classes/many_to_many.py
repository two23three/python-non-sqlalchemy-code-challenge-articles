class Article:
    all= []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = str(title)
        Article.all.append(self)
    #this method is a getter for the title attribute
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        return self.title
        
     

class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name

    def articles(self):
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        articles = Article(self, magazine, title)
        return articles

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    def contributing_authors(self):
        return [authors for authors in Author.all if len(authors.articles()) > 0]

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @name.setter
    def name(self, new_names):
        if isinstance(new_names, str):
            if 2 <= len(new_names) <= 16:
                self._name = new_names
        return self._name
    
    @category.setter
    def category(self, new_categories):
        if isinstance(new_categories, str):
            if len(new_categories) > 0:
                self._category = new_categories
        return self._category
    
    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None
   
    def contributing_authors(self):
      authors = {}
      for article in self.articles():
          if article.author in authors:
              authors[article.author] += 1
          else:
              authors[article.author] = 1
      contributing_authors = [author for author, count in authors.items() if count >= 2]
      return contributing_authors if contributing_authors else None




# Create instances of authors
author1 = Author("John Doe")
author2 = Author("Jane Smith")
author3 = Author("Alice Johnson")

# Create instances of magazines
magazine1 = Magazine("Science Today", "Science")
magazine2 = Magazine("Tech News", "Technology")

# Add articles to the magazines
author1.add_article(magazine1, "The Latest Discoveries in Physics")
author1.add_article(magazine2, "Advancements in Artificial Intelligence")
author2.add_article(magazine1, "The Future of Space Exploration")
author3.add_article(magazine1, "Understanding Quantum Mechanics")
author3.add_article(magazine2, "The Rise of Cybersecurity")
# Add more articles to Magazine 1 by existing authors
author1.add_article(magazine1, "New Developments in Astrophysics")
author2.add_article(magazine1, "Exploring Mars: Recent Findings")

contributing_authors = magazine1.contributing_authors()

if contributing_authors:
    print("Authors who have written more than two articles for Magazine 1:")
    for author in contributing_authors:
        print(author.name)
else:
    print("No authors found who have written more than two articles for Magazine 1")

