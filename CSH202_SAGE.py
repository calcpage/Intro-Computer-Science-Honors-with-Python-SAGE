#CSH202 What's A CPU? 2019.1018
show('#1) Von Neumann Machine')
show('#1) CPU = Central Processing Unit')
show('#1) ALU = Arithmetic & Logic Unit')
show('#1) MU = Memory Unit')
show('#1) I/O = Input/Output Unit')
show('#1) MANIAC, ENIAC, UNIVAC, Harvard Mark I')
show('')
show('#2) RAM = Random Access Memory (choice D)')
show('')
show('#3) How much bigger is 120GB as compared to 512MB')
show('120 GigaBytes = ', 120*1000^3)
show('120 GibiBytes = ', 120*1024^3)
show('512 MegaBytes = ', 512*1000^2)
show('512 MebiBytes = ', 512*1024^2)
show('120 GigaBytes/512 MegaBytes =',n(120*1000^3/(512*1000^2)))
show('120 GibiBytes/512 MebiBytes =',n(120*1024^3/(512*1024^2)))
show('')
show('#4) how many values can be encoded in 2bits, 3bits or 1byte?')
show('#4) 2bits: 00,01,10,11 - 2^n where n=2: ', 2^2)
show('#4) 3bits: 000,001,010,011,100,101,110,111 - 2^n where n=3: ', 2^3)
show('#4) 1bytes = 8bits - 2^n where n=8:', 2^8)
show('#4) largest 2 bit value = ', 2^2-1)
show('#4) largest 3 bit value = ', 2^3-1)
show('#4) largest 8 bit value = ', 2^8-1)
show('')
show('#5) is a byte enough to hold all ASCII character?')
show('#5) yes, because 2^8 =',2^8)
show('#5) if you are encoding your keyboard, you need 7bits, 2^7=',2^7)