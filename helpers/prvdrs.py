class Prvdrs:
    prvdrs = {
            'outook_prvdr':'smtp-mail.outlook.com', 
            'gmail_prvdr':'smtp.gmail.com'
            }

    def opt(self, provider):
        if provider == 'outlook':
            return self.prvdrs['outook_prvdr']
        elif provider == 'gmail':
            return self.prvdrs['gmail_prvdr']
        else:
            return 'outook_prvdr'
