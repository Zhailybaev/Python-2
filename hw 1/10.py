day=int(input("Input birthday: "))
month=input("Input month of birth (e.g. march, july etc): ")
sign=''
if month=="january":
    if day>19:
        sign="Aquarius"
    else:
        sign="Capricornus"
if month=="february":
    if day>18:
        sign="Pisces "
    else:
        sign="Aquarius"
if month=="march":
    if day>20:
        sign="Aries"
    else:
        sign="Pisces"
if month=="april":
    if day>19:
        sign="Taurus"
    else:
        sign="Aries"
if month=="may":
    if day>20:
        sign="Gemini"
    else:
        sign="Taurus"
if month=="june":
    if day>21:
        sign="Cancer"
    else:
        sign="Gemini"
if month=="july":
    if day>22:
        sign="Leo"
    else:
        sign="Cancer"
if month=="august":
    if day>22:
        sign="Virgo"
    else:
        sign="Leo"
if month=="september":
    if day>22:
        sign="Libra"
    else:
        sign="Virgo"
if month=="october":
    if day>23:
        sign= "Scorpius"
    else:
        sign="Libra"
if month=="november":
    if day>21:
        sign= "Sagittarius"
    else:
        sign="Scorpius"
if month=="december":
    if day>21:
        sign= "Capricornus"
    else:
        sign="Sagittarius"

print("Your Astrological sign is:", sign)
