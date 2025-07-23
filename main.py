 # sync example:

import time

 #step 1:
print("pani ubalna shuru...")
time.sleep(5)
print("pani ubal gaya.")

 #step 2:
print("Roti banana shuru...")
time.sleep(3)
print("Roti ban gayi.")

#async example:

import asyncio

async def pani_ubalo():
    print("pani ubalna shuru...")
    await asyncio.sleep(5)
    print("pani ubal gaya.")   


async def roti_banao():
    print("Roti banana shuru...")
    await asyncio.sleep(3)
    print("Roti ban gay.") 

async def main(): 
    await asyncio.gather(
        pani_ubalo(),
        roti_banao()
    )
asyncio.run(main())

