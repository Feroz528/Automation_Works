f=open("/home/root_EB/CP_UNDEPLOY.txt","w+")

sh_13=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 1.3 ]')
print >> f, sh_13
da_13=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 1.3]') 
print >> f, da_13
st_13=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 1.3]')
print >> f, st_13
un_13=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 1.3]')
print >> f, un_13
del_13=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 1.3]')
print >> f, del_13

sh_24=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.4 ]')
print >> f, sh_24
da_24=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.4]') 
print >> f, da_24
st_24=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.4]')
print >> f, st_24
un_24=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.4]')
print >> f, un_24
del_24=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.4]')
print >> f, del_24

sh_CPMS202=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS202 ]')
print >> f, sh_CPMS202
da_CPMS202=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS202]') 
print >> f, da_CPMS202
st_CPMS202=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS202]')
print >> f, st_CPMS202
un_CPMS202=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS202]')
print >> f, un_CPMS202
del_CPMS202=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms CPMS202]')
print >> f, del_CPMS202

sh_25=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.5 ]')
print >> f, sh_25
da_25=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.5]') 
print >> f, da_25
st_25=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.5]')
print >> f, st_25
un_25=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.5]')
print >> f, un_25
del_25=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.5]')
print >> f, del_25

sh_26=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.6 ]')
print >> f, sh_26
da_26=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.6]') 
print >> f, da_26
st_26=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.6]')
print >> f, st_26
un_26=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.6]')
print >> f, un_26
del_26=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.6]')
print >> f, del_26

sh_27=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.7 ]')
print >> f, sh_27
da_27=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.7]') 
print >> f, da_27
st_27=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.7]')
print >> f, st_27
un_27=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.7]')
print >> f, un_27
del_27=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.7]')
print >> f, del_27

sh_28=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.8 ]')
print >> f, sh_28
da_28=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.8]') 
print >> f, da_28
st_28=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.8]')
print >> f, st_28
un_28=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.8]')
print >> f, un_28
del_28=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.8]')
print >> f, del_28

sh_29=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.9 ]')
print >> f, sh_29
da_29=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.9]') 
print >> f, da_29
st_29=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.9]')
print >> f, st_29
un_29=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.9]')
print >> f, un_29
del_29=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.9]')
print >> f, del_29

sh_210=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym 2.10 ]')
print >> f, sh_210
da_210=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.10]') 
print >> f, da_210
st_210=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.10]')
print >> f, st_210
un_210=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym 2.10]')
print >> f, un_210
del_210=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms 2.10]')
print >> f, del_210

sh_CPMS2_2=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_2 ]')
print >> f, sh_CPMS2_2
da_CPMS2_2=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_2]') 
print >> f, da_CPMS2_2
st_CPMS2_2=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_2]')
print >> f, st_CPMS2_2
un_CPMS2_2=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_2]')
print >> f, un_CPMS2_2
del_CPMS2_2=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms CPMS2_2]')
print >> f, del_CPMS2_2

sh_CPMS2_5=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_5 ]')
print >> f, sh_CPMS2_5
da_CPMS2_5=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_5]') 
print >> f, da_CPMS2_5
st_CPMS2_5=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_5]')
print >> f, st_CPMS2_5
un_CPMS2_5=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_5]')
print >> f, un_CPMS2_5
del_CPMS2_5=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms CPMS2_5]')
print >> f, del_CPMS2_5

sh_CPMS2_6=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_6 ]')
print >> f, sh_CPMS2_6
da_CPMS2_6=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_6]') 
print >> f, da_CPMS2_6
st_CPMS2_6=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_6]')
print >> f, st_CPMS2_6
un_CPMS2_6=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_6]')
print >> f, un_CPMS2_6
del_CPMS2_6=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms CPMS2_6]')
print >> f, del_CPMS2_6

sh_CPMS2_7=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_7 ]')
print >> f, sh_CPMS2_7
da_CPMS2_7=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_7]') 
print >> f, da_CPMS2_7
st_CPMS2_7=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_7]')
print >> f, st_CPMS2_7
un_CPMS2_7=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym CPMS2_7]')
print >> f, un_CPMS2_7
del_CPMS2_7=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms CPMS2_7]')
print >> f, del_CPMS2_7
