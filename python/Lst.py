i=0
nama=[]
nim=[]
Tugas=[]
Uts=[]
Uas=[]
Rt=[]
while True:
    print 'Masukkan data ke - ',i+1
    nama.append(raw_input('Nama Anda : '))
    nim.append(raw_input('NIM Anda : '))
    Tugas.append(input('Nilai Tugas : '))
    Uts.append(input('Nilai Uts : '))
    Uas.append(input('Nilai Uas : '))
    if len(nim[i])!=3:
        print 'NIM Salah'
        Rt = float (Tugas+Uts+Uas)/3
    lagi=''
    while lagi!='y' and lagi!='t':
        lagi=raw_input('INPUT LAGI [Y/T] : ')
    i+=1
    if lagi=='t':
        break
print '========================================================================'
print 'No. | Nama     | NIM    | Tugas  Uts  Uas  Akhir'
print '========================================================================'
for n in range(i):
    print '%3d | %-10s | %-6s | %4d | %4d | % 4d | %4d |' % (n+1, nama[n], nim[n], Tugas[n], Uts[n], Uas[n], Rt[n])
#    print n+1,'  ',nama[n],'  ',nim[n],'  ',Tugas[n],'  ',Uts[n],'  ',Uas[n],'  ',Rata[n],''