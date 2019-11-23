import config

def emailTemplate(obj):
    headerText = obj.headerText
    paragraphText = obj.paragraphText
    buttonLink = obj.buttonLink
    buttonText = obj.buttonText
    socialIcons = createSocialIcons()
    addressSection = createAddressSection()

    htmlString = """

        <!doctype html>

        <html lang="en">

        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Podverse</title>
            <style>
            body {{
                margin: 0;
                padding: 0;
            }}
            .container {{
                background-color: #D8D8D8;
                font-family: "Arial", sans-serif;
                margin: 0;
                padding: 0 0 32px 0;
            }}
            .nav {{
                background-color: {0};
                height: 58px;
                text-align: center;
                width: 100%;
            }}
            .nav img {{
                height: 38px;
                margin-top: 10px
            }}
            .content {{
                background-color: #FFF;
                margin: 40px auto;
                max-width: 380px;
                padding: 40px 40px 48px 40px;
            }}
            .content h1 {{
                color: {0};
                font-size: 30px;
                margin: 0 0 32px 0;
                text-align: center;
            }}
            .content p {{
                color: #000;
                font-size: 14px;
                margin: 0 0 32px 0;
                text-align: center;
            }}
            .content .button {{
                background-color: {0};
                border-radius: 100px;
                color: #FFF;
                display: block;
                font-size: 14px;
                height: 40px;
                line-height: 40px;
                text-align: center;
                text-decoration: none;
                width: 100%;
            }}
            .content .closing {{
                margin: 36px 0 0 0;
                text-align: center;
            }}
            .footer .social-icons {{
                margin: 36px 32px 28px 32px;
                text-align: center;
            }}
            .footer .social-icon {{
                display: inline-block;
                height: 32px;
                margin: 0 16px;
                width: 32px;
            }}
            .footer .social-icon img {{
                height: 32px;
                width: 32px;
            }}
            .footer .address {{
                color: #555;
                font-size: 14px;
                line-height: 20px;
                margin: 0;
                text-align: center;
            }}
            .footer .unsubscribe {{
                color: #555;
                display: block;
                font-size: 12px;
                margin: 32px 0 0 0;
                text-align: center;
                text-decoration: none;
            }}
            </style>
        </head>

        <body>
            <div class="container">
            <div class="nav">
                <img src="{1}" />
            </div>
            <div class="content">
                <h1>{2}</h1>
                <p>{3}</p>
                <a class="button" href="{4}">{5}</a>
            </div>
            <div class="footer">
                {6}
                {7}
            </div>
            </div>
        </body>

        </html>
    """

    htmlString = htmlString.format(config.EMAIL_BRAND_COLOR, config.EMAIL_HEADER_IMAGE_URL, headerText, paragraphText, buttonLink, buttonText, socialIcons, addressSection)

    return htmlString

class EmailTemplateObj:
    def __init__(self, headerText, paragraphText, buttonLink, buttonText):
        self.headerText = headerText
        self.paragraphText = paragraphText
        self.buttonLink = buttonLink
        self.buttonText = buttonText

def createAddressSection():
    htmlString = """
        <div class="address">
            {0}
            <br />
            {1}
        </div>
    """
    htmlString = htmlString.format(config.LEGAL_NAME, config.LEGAL_ADDRESS)
    return htmlString

def createFacebookIcon():
    htmlString = """
        <a class="social-icon" href="{0}">
            <img src="{1}" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_FACEBOOK_PAGE_URL, config.SOCIAL_FACEBOOK_IMAGE_URL)
    return htmlString

def createGithubIcon():
    htmlString = """
        <a class="social-icon" href="{0}">
            <img src="{1}" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_GITHUB_PAGE_URL, config.SOCIAL_GITHUB_IMAGE_URL)
    return htmlString

def createRedditIcon():
    htmlString = """
        <a class="social-icon" href="{0}">
            <img src="{1}" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_REDDIT_PAGE_URL, config.SOCIAL_REDDIT_IMAGE_URL)
    return htmlString

def createTwitterIcon():
    htmlString = """
        <a class="social-icon" href="{0}">
            <img src="{1}" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_TWITTER_PAGE_URL, config.SOCIAL_TWITTER_IMAGE_URL)
    return htmlString

def createSocialIcons():
    facebookIcon = createFacebookIcon()
    githubIcon = createGithubIcon()
    redditIcon = createRedditIcon()
    twitterIcon = createTwitterIcon()

    htmlString = """
        <div class="social-icons">
            {0}
            {1}
            {2}
            {3}
        </div>
    """
    htmlString = htmlString.format(facebookIcon, githubIcon, redditIcon, twitterIcon)
    return htmlString
