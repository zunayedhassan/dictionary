__author__ = 'Zunayed Hassan'

"""
AboutBoxInfo(
    (String)         Application Name
    (String)         Version
    (String)         AppDesc
    (String)         License
    (AuthorsInfo []) Authors
)
"""
class AboutBoxInfo():
    ApplicationName = None
    Version         = None
    AppDesc         = None
    License         = None
    Icon            = None
    AuthorsList     = []    # List of 'Authors Info'
    
    
"""
AuthorsInfo(
    (String)        Contribution
    (AuthorInfo []) Authors
)
"""
class AuthorsInfo():
    Contribution = None
    Authors      = []       # List of 'Author Info'
    

"""
CONSTRUCTOR:    AuthorInfo(
                    (String) Name
                    (String) Website
                    (String) Email
                )
"""    
class AuthorInfo():
    def __init__(self, name, website = None, email = None):
        self.Name    = name
        self.Website = website
        self.Email   = email
            
    def __str__(self):
        return (str(self.Name) + "\t" + str(self.Email) + "\t" + str(self.Website))
    