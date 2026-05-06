class web_developer:
    def __init__(self,role,language):
        self.role = role
        self.language = language


    def show_details(self):
        return f"Hi it's Yan. I am a {self.role} and I use the {self.language} programming language for web design work.."

    def kaka(self):
        return f"Hi it's omur. I am a {self.role} and I use the {self.language} programming language for web design work.."


aboutObj = web_developer("web_developer","Python")
print(aboutObj.show_details())
ab_Obj = web_developer("web_developer","Python")
print(ab_Obj.kaka())
