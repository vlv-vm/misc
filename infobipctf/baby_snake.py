from base64 import b64decode
exec("exec(b64decode('ZnJvbSBvcGVyYXRvciBpbXBvcnQgYWRkLHhvcixuZSxlcTtPPWNocjtPTz1vcmQ7TzA9aW5wdXQ7T09PPWFkZDtPME89eG9yO09PMD1pbnQ7TzAwPXN0cigpLmpvaW47TzBPMD1wcmludDtPTzAwPW5lO08wMDA9cmFuZ2U7TzBPTz1PMChPT08oTyhPME8oMHgwMDAwMDAwNywweDAwMDAwMDY2KSksTyhPT08oMHgwMDAwMDAwMzYsMHgwMDAwMDAwNCkpKSk7T08wTz1PTzAoTzAoT09PKE8oT09PKDB4MDAwMDAwMDcsMHgwMDAwMDA1YikpLE8oTzBPKDB4MDAwMDAwM2UsMHgwMDAwMDAwNCkpKSkpO08wTzAoTzAwKFtPKE8wTyhPTyhPME9PW08wME9dKSwgT08wTykpIGZvciBPMDBPIGluIE8wMDAoTzBPKDB4MDAwMDAwMjAsMHgwMDAwMDAwMCkpXSkpCmlmIE9PMDAoT08wTzw8MHgyLE9PTygweDAwMDAwMDAxLDB4MDAwMDAwN2IpKTpyYWlzZQppZiBPTzAwKE8wT09bMHgwMDAwMDAxMToweDAwMDAwMDFhXSxPT08oTygweDAwMDAwMDQwKSxPT08oTygweDAwMDAwMDZjKSxPT08oTygweDAwMDAwMDJjKSxPT08oTygweDAwMDAwMDY5KSxPT08oTygweDAwMDAwMDJjKSxPT08oTygweDAwMDAwMDZkKSxPT08oTygweDAwMDAwMDZhKSxPT08oTygweDAwMDAwMDZjKSxPKDB4MDAwMDAwNDApKSkpKSkpKSkpOnJhaXNlCk9PMDBPMD1bMHgwMDAwMDAwNiwweDAwMDAwMDBiLDB4MDAwMDAwMGMsMHgwMDAwMDAxMSwweDAwMDAwMDFhLDB4MDAwMDAwMWZdCmZvciBPMDBPIGluIE8wMDAoMHgwMDAwMDAwMCwgMHgwMDAwMDAwNiwgMHgwMDAwMDAwMik6IAoJaWYgT08wMChPME9PW09PMDBPMFtPMDBPXTpPTzAwTzBbT09PKE8wME8sMHgwMDAwMDAwMSldXSxPT08oTygweDAwMDAwMDZjKSxPT08oTygweDAwMDAwMDcxKSxPT08oTygweDAwMDAwMDdlKSxPT08oTygweDAwMDAwMDc0KSxPKDB4MDAwMDAwN2EpKSkpKSk6cmFpc2UKaWYgT08wMChPTzAoTzBPT1sweDAwMDAwMDBiXSksMHgwMDAwMDAwMik6cmFpc2UKCg=='))")

####################################################################
from operator import add,xor,ne,eq;
O=chr;
OO=ord;
O0=input;
OOO=add;
O0O=xor;
OO0=int;
O00=str().join;
O0O0=print;
OO00=ne;
O000=range;
O0OO=O0(OOO(O(O0O(0x00000007,0x00000066)),O(OOO(0x000000036,0x00000004)))); # O0OO=input('a:'); O0OO = first
OO0O=OO0(O0(OOO(O(OOO(0x00000007,0x0000005b)),O(O0O(0x0000003e,0x00000004))))); # OO0O=int(input('b:'));  OO0O = second
O0O0(O00([O(O0O(OO(O0OO[O00O]), OO0O)) for O00O in range(O0O(0x00000020,0x00000000))])) # print(str().join([chr(xor(ord(input('a:')[O00O]), int(input('b:')))) for O00O in range(32)]))
#O00O = i


if ne(OO0O<<0x2,OOO(0x00000001,0x0000007b)):
    raise
if ne(O0OO[0x00000011:0x0000001a],OOO(O(0x00000040),OOO(O(0x0000006c),OOO(O(0x0000002c),OOO(O(0x00000069),OOO(O(0x0000002c),OOO(O(0x0000006d),OOO(O(0x0000006a),OOO(O(0x0000006c),O(0x00000040)))))))))):
    raise 

OO00O0=[0x00000006,0x0000000b,0x0000000c,0x00000011,0x0000001a,0x0000001f] # array=[0x00000006,0x0000000b,0x0000000c,0x00000011,0x0000001a,0x0000001f]

for O00O in O000(0x00000000, 0x00000006, 0x00000002): 
	if ne(O0OO[array[O00O]:array[OOO(O00O,0x00000001)]],OOO(O(0x0000006c),OOO(O(0x00000071),OOO(O(0x0000007e),OOO(O(0x00000074),O(0x0000007a)))))):
        raise

#####################################################################

first=input('a:')
second=int(input('b:'))
print("".join([chr(xor(ord(first[i]), second)) for i in range(32)]))

#bitwise shift left 
#second=31
if ne(second<<0x2, 124): 
    raise

#[17:26]
if ne(first[0x00000011:0x0000001a],'@l,i,mjl@'): 
    raise

#array=[6, 11, 12, 17, 26, 31]
array=[0x00000006,0x0000000b,0x0000000c,0x00000011,0x0000001a,0x0000001f] 

##range(0,6,2)
for i in range(0x00000000, 0x00000006, 0x00000002): 
	if ne(first[array[i]:array[add(i,0x00000001)]],'lq~tz'):
        raise
    if ne(int(first[11]), 2):
        raise


#prvi if
first='@l,i,mjl@' #17:26

#drugi if
first = 'la~rzglq~tzglq~tz@l,i,mjl@lq~tz'

#'000000lq~tz0lq~tz@l,i,mjl@lq~tz0'
'000000lq~tz2lq~tz@l,i,mjl@lq~tz0'
[0:6] [11:12] [31:32]





