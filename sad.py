import urllib2, re, webbrowser, time

def depression():
    """
    spams pics of Mark Z in you browser.
    
    I am sorry
    """
    soup = urllib2.urlopen("http://www.dogpile.com/info.dogpl.t10.1/search/images?q=mark%20zuckerberg&fcoid=408&fcop=topnav&fpid=2").read()

    stack = []

    find_imgs = re.compile('img src=(.*)/>')
    luck = re.findall(find_imgs, str(soup))
    for x in luck[3:-5]:
        y = str(x).split(" ")[0]
    
        stack.append(y)
    return stack


if __name__ == '__main__':
    depression()