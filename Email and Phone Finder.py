#Regex example program: phone and email scraper 
#! python3
import re, pyperclip

#Create a regex Obj for phone numbers
PhoneRegex = re.compile(r'''
#example phone numbers: 0411 848 345, +61 411 848 345, 9704 6465, (03) 9704 6465, 03 9704 6465        
(
(\s)?
(((\+)?\d\d)|(\(\d\d\))|(\d\d))?        #Area code or extension (optional). This group may appear 0 or 1 times
(\s)?                                   #first space (will not feature a '-')
(\d{3,4})                               #first 3-4 digits
(\s|-)?                                 #second space (may use a dash to space instead of actual spacing)
(\d{3,4})                               #middle 3-4 digits (this will be the end for Landline numbers)
(\s|-)?                                 #third space
(\d{0,4})                               #last digits for mobile numbers (this should hopefully catch the final 3 digits for mobile numbers)
)
''', re.VERBOSE)

#Create a regex Obj for email addresses
EmailRegex = re.compile(r'''
#email example: some.+_thing@domain((\d{2,5})?).com                        
[a-zA-Z0-9_.+]+          #name part (can find lowercase, caps, numbers and those symbols)
@                        #@ symbol
[a-zA-Z0-9_.+]+          #domain name part
''', re.VERBOSE)

#Get text off the clipboard
text = pyperclip.paste()

#Extract the email/phone numbers from this text
ExtractedPhone = PhoneRegex.findall(text)
ExtractedEmail = EmailRegex.findall(text)

AllPhoneNumbers = []
for PhoneNumber in ExtractedPhone: 
    AllPhoneNumbers.append(PhoneNumber[0])
#print(ExtractedEmail, ExtractedPhone)

#Copy the extracted email/phone to the clipboard.
results = '\n'.join(AllPhoneNumbers) + '\n' + '\n'.join(ExtractedEmail)
pyperclip.copy(results)
