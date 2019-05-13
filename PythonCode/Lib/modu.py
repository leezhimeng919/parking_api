#_*_ coding:utf-8_*_ 
import EP_checkOutLib

EP_checkOutLib.checkOutWorkingStatus(2641)

# print EP_checkOutLib.getContractPlateList(2642)

# print EP_checkOutLib.delOneContractPlate(2642,'粤B10007')

# print EP_checkOutLib.recoverOneContractPlate(2642,'粤B10007')

print EP_checkOutLib.getInviteCarPlateList(2642)

# print EP_checkOutLib.getAuthorizeIdByPlate(2642,'粤V12345')

print EP_checkOutLib.setInviteCarPlate(2642,"2019-04-11 14:00:00","2019-04-16 14:00:00",'1','粤B12353')

# print EP_checkOutLib.delInviteCarPlate(2642,'粤V12345')

print EP_checkOutLib.setGateOpen(2642, '粤V12345')