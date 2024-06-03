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
    # Setter for the title attribute with validation
    @title.setter
    def title(self, title):
       if hasattr(self,"title"):AttributeError("Title cannot be changed")
       else:
            if isinstance(title,str):
                if 5<=len(title)<=50:
                    self._title=title
                else:ValueError("Title must be between 5 and 50 characheters")
            else:TypeError("Title must be a string")
  
    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise TypeError("Author must be of type Author")
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise TypeError("Magazine must be of type Magazine")
     

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
    # Method to get all articles written by the author
    def articles(self):
        return [articles for articles in Article.all if articles.author == self]

    # Method to get all unique magazines the author has contributed to
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    # Method to add a new article for the author
    def add_article(self, magazine, title):
        articles = Article(self, magazine, title)
        return articles
   
    # Method to get all unique  categories of magazines the author has written for
    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

   

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
    
    # Setter for the name attribute with validation
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
   
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")
    
    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None
   
    def contributing_authors(self):
     #initialise an empty dictionary
      authors = {}
      # iterate over articles of teh current magazine
      for article in self.articles():
          #check if the author is already in the dictionary
          if article.author in authors:
              #increase the count
              authors[article.author] += 1
          else:
              authors[article.author] = 1
      #create a list of authors who have written more than 2 articles
      contributing_authors = [author for author, count in authors.items() if count >= 2]
      return contributing_authors if contributing_authors else None
    
   
    @staticmethod
    def top_publisher():
       #check if there are any articles
        if Article.all:
            #initialise an empty dictionary
            magazine_article_count = {}
            
            # iterate over articles
            for article in Article.all:
                #get the magazine of the article 
                magazine = article.magazine
                #check if the magazine is already in the dictionary
                if magazine in magazine_article_count:
                    #increase the count
                    magazine_article_count[magazine] += 1
                else:
                   magazine_article_count[magazine] = 1
            
           # return the magazine with the most articles
            return max(magazine_article_count, key=magazine_article_count.get)
        return None

    


# Create instances of authors
author1 = Author("Tulley Mwenda")
author2 = Author("Maureen Murimi")
author3 = Author("Victor ")

# Create instances of magazines
magazine1 = Magazine("Science Today", "Science")
magazine2 = Magazine("Tech News", "Technology")

# Add articles to the magazines
author1.add_article(magazine1, "The Latest Discoveries in Physics")
author1.add_article(magazine2, "Advancements in Cancer Treatment")
author2.add_article(magazine1, "The Future of Deep sea Exploration")
author3.add_article(magazine1, "Understanding Mechanics")
author3.add_article(magazine2, "The Rise of Cybercrime")
# Add more articles to Magazine 1 by existing authors
author1.add_article(magazine1, "New Developments in Tech")
author2.add_article(magazine1, "Exploring Oceans: Recent Findings")

contributing_authors = magazine1.contributing_authors()

if contributing_authors:
    print("Authors who have written more than two articles for Magazine one:")
    for author in contributing_authors:
        print(author.name)
else:
    print("No authors found who have written more than two articles for Magazine1")

top_publisher = Magazine.top_publisher()

# Print information about the top publisher
if top_publisher:
    print(f"The Magazine with the most articles is: {top_publisher.name}")
    print(f"Category: {top_publisher.category}")
else:
    print("No articles found.")
    