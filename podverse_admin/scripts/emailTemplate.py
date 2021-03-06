import config

def emailTemplate(obj):
    headerText = obj.headerText
    paragraphText = obj.paragraphText
    buttonLink = obj.buttonLink
    buttonText = obj.buttonText
    socialIcons = createSocialIcons()
    addressSection = createAddressSection()

    # All styles must be inline.
    # <style> tags are not reliably supported by Gmail.
    htmlString = """

        <!doctype html>

        <html lang="en">

        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Podverse</title>
        </head>

        <body style="margin: 0; padding: 0;">
            <div class="container" style="background-color: #D8D8D8; font-family: 'Arial', sans-serif; margin: 0; padding: 0 0 32px 0;">
            <div class="nav" style="background-color: {0}; height: 58px; text-align: center; width: 100%;">
                <img src="{1}" style="height: 38px; margin-top: 10px; max-width: 280px;" />
            </div>
            <div class="content" style="background-color: #FFF; margin: 40px auto; max-width: 380px; padding: 40px 40px 48px 40px;">
                <h1 style="color: {0}; font-size: 30px; margin: 0 0 32px 0; text-align: center;">{2}</h1>
                <p style="color: #000; font-size: 16px; margin: 0 0 32px 0; text-align: center;">{3}</p>
                <a class="button" href="{4}" style="background-color: {0}; border-radius: 100px; color: #FFF; display: block; font-size: 16px; height: 40px; line-height: 40px; text-align: center; text-decoration: none; width: 100%;">{5}</a>
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
        <div class="address" style="color: #555; font-size: 14px; line-height: 20px; margin: 0; text-align: center;">
            {0}
            <br />
            {1}
        </div>
    """
    htmlString = htmlString.format(config.LEGAL_NAME, config.LEGAL_ADDRESS)
    return htmlString

def createFacebookIcon():
    htmlString = """
        <a class="social-icon" href="{0}" style="display: inline-block; height: 32px; margin: 0 16px; width: 32px;">
            <img src="{1}" style="height: 32px; width: 32px;" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_FACEBOOK_PAGE_URL, config.SOCIAL_FACEBOOK_IMAGE_URL)
    return htmlString

def createGithubIcon():
    htmlString = """
        <a class="social-icon" href="{0}" style="display: inline-block; height: 32px; margin: 0 16px; width: 32px;">
            <img src="{1}" style="height: 32px; width: 32px;" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_GITHUB_PAGE_URL, config.SOCIAL_GITHUB_IMAGE_URL)
    return htmlString

def createLinkedInIcon():
    htmlString = """
        <a class="social-icon" href="{0}" style="display: inline-block; height: 32px; margin: 0 16px; width: 32px;">
            <img src="{1}" style="height: 32px; width: 32px;" />
        </a>
    """
    htmlString = htmlString.format(
        config.SOCIAL_LINKEDIN_PAGE_URL, config.SOCIAL_LINKEDIN_IMAGE_URL)
    return htmlString

def createRedditIcon():
    htmlString = """
        <a class="social-icon" href="{0}" style="display: inline-block; height: 32px; margin: 0 16px; width: 32px;">
            <img src="{1}" style="height: 32px; width: 32px;" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_REDDIT_PAGE_URL, config.SOCIAL_REDDIT_IMAGE_URL)
    return htmlString

def createTwitterIcon():
    htmlString = """
        <a class="social-icon" href="{0}" style="display: inline-block; height: 32px; margin: 0 16px; width: 32px;">
            <img src="{1}" style="height: 32px; width: 32px;" />
        </a>
    """
    htmlString = htmlString.format(config.SOCIAL_TWITTER_PAGE_URL, config.SOCIAL_TWITTER_IMAGE_URL)
    return htmlString

def createSocialIcons():
    facebookIcon = createFacebookIcon()
    githubIcon = createGithubIcon()
    linkedinIcon = createLinkedInIcon()
    redditIcon = createRedditIcon()
    twitterIcon = createTwitterIcon()

    htmlString = """
        <div class="social-icons" style="margin: 36px 32px 28px 32px; text-align: center;">
            {0}
            {1}
            {2}
            {3}
            {4}
        </div>
    """
    htmlString = htmlString.format(facebookIcon, githubIcon, linkedinIcon, redditIcon, twitterIcon)
    return htmlString
