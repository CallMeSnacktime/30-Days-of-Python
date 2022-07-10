msg_template="""Hello {name},
Thank you for joining {website}. We are very 
happy to have you wtith us
""" #.format(name="Justing", website='cfe.sh')

def format_msg(my_name="Atiba", my_website="cfe.sh"):
    my_msg=msg_template.format(name=my_name,  website=my_website)
    #print(my_msg)
    return my_msg
