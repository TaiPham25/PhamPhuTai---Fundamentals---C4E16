import pyexcel

a_list_of_dictionary = [
    {
        'title' : 'hom nay troi dep',
        'link' : 'https://www.google.com.vn'
    },
    {
        'title' : 'hom nay troi dep',
        'link' : 'https://www.google.com.vn'
    },
    {
        'title' : 'hom nay troi dep',
        'link' : 'https://www.google.com.vn'
    }

]
pyexcel.save_as(records=a_list_of_dictionary, dest_file_name="text.xlsx")
