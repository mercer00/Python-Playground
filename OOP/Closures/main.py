# html tag printer using closures

def html_tag(tag):
    def element(text):
        print(f"<{tag}>{text}</{tag}>")
    return element


print_heading = html_tag("h1")
print_heading("Hello world")
print_heading("SimplyRecipes")

print_paragraph = html_tag("p")
print_paragraph("Lorem ipsum dollar")
print_paragraph("This theme looks dope")
