import pg
# db.debug = True

db = pg.DB(dbname='phonebook')

# query = db.query('select * from album')
# print query
# result_list = query.namedresult()
# for result in result_list:
#     print "Album %s phone_number in %s" % (result.name, result.phone_number)
#
# db.insert('phonebook', name = raw_input("the name?").lower(), phone_number='raw_input("the number?").lower()'', email = raw_input("the email?").lower())
#
# db.update('phonebook', {
#     'id': 1, 'name': "Led Zeppelin V", 'phone_number': "2417-11-08"
# })
#
# db.delete('song', {'id': 3})
#
# CREATE TABLE phonebook (
#     id serial PRIMARY KEY,
#     name varchar NOT NULL UNIQUE,
#     phone_number varchar,
#     email varchar UNIQUE
# );


def lookup():
    name = raw_input("the name?").lower()
    result_list = db.query("select * from phonebook where name ilike '%s'" % name).namedresult()
    for result in result_list:
        print "%s's phone number is %s" % (result.name, result.phone_number)

def set_entry():
    name = raw_input('Name? ').lower()
    number = raw_input('Number ')
    email = raw_input('email? ')
    result_list = db.query("select id from phonebook where name ilike '%s'" % name).namedresult()
    if len(result_list) > 0:
        id = result_list[0].id
        db.update('phonebook', {
            'id' : id,
            'name': name,
            'phone_number': number,
            'email': email
        })
        print "Stored %s's number." % name
    else:
        db.insert('phonebook', name=name, phone_number=number, email=email)
        print 'Added entry for %s' % name

def delete_entry():
    name = raw_input("What's the name to delete?").lower()
    #V1 delete from phonebook where name = '%s' % name
    result_list = db.query("select id from phonebook where name ilike '%s'" % name).namedresult()
    id = result_list(0).id
    print "ID is %d" % id
    db.delete('phonebook', {'id': id})
    print '%s deleted' % name


def list_all():
    result_list = db.query('select * from phonebook').namedresult()
    for result in result_list:
        print "%s's phone number is %s" % (result.name, result.phone_number)

def quit():
    print '''Phonebook put away'''
    return False
active = True
while active == True:
    print "Electronic Phone Book"
    print "====================="
    print ("1\. Look up an entry")
    print ("2\. Set an entry")
    print ("3\. Delete an entry")
    print ("4\. List all entries")
    print ("5\. Quit")

    response = int(raw_input("What do you want to do? (1-5)"))

    if response == 1:
        lookup()
    elif response == 2:
        set_entry()
    elif response == 3:
        delete_entry()
    elif response == 4:
        list_all()
    elif response == 5:

        active = quit()
