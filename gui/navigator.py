class Navigator:

    def __init__(
        self, 
        root,
        db,
        pages # dict mapping route to class name
    ):
        self.root = root
        self.pages = pages
        self.db = db

        home_page = self.pages["/"](root, db, self)
        home_page.pack()

        self.current_page = home_page

    def go_to_route(self, route):
        new_page = self.pages[route](self.root, self.db, self)
        new_page.pack()

        if hasattr(self, "current_page"):
            self.current_page.destroy()
        
        self.current_page = new_page
        
    def go_to_route_with_data(self, route, data):
        new_page = self.pages[route](self.root, self.db, self, data=data)
        new_page.pack()

        if hasattr(self, "current_page"):
            self.current_page.destroy()
        
        self.current_page = new_page
