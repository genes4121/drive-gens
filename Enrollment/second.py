

from tkinter import *
import sys
import mysql.connector
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
import Enrollment.PSB as PSB
import second_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    second_support.set_Tk_var()
    top = Toplevel1 (root)
    second_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    second_support.set_Tk_var()
    top = Toplevel1 (w)
    second_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def __init__(self, top=None):
        # Radios Value Initialization
        self.jk = StringVar()
        self.school = StringVar()
        self.tp = StringVar()

        # Combo Boxes Value Intialization
        self.tgl = StringVar()
        self.bln = StringVar()
        self.thn = StringVar()

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1060x602+98+107")
        top.minsize(116, 1)
        top.maxsize(1362, 742)
        top.resizable(0, 0)
        top.title("Pendaftaran Siswa Baru SMK Cyber Media Utama Tahun 2020")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#b7ffb3")
        top.configure(highlightcolor="black")

        self.tag_pendaftaran = ttk.Label(top)
        self.tag_pendaftaran.place(relx=0.009, rely=-0.017, height=59, width=376)

        self.tag_pendaftaran.configure(background="#d9d9d9")
        self.tag_pendaftaran.configure(foreground="#000000")
        self.tag_pendaftaran.configure(font="-family {Titillium} -size 16 -weight bold")
        self.tag_pendaftaran.configure(relief="flat")
        self.tag_pendaftaran.configure(text='''Form Pendaftaran Calon Siswa Baru''')

        self.verify_code_status = ttk.Label(top)
        self.verify_code_status.place(relx=0.009, rely=0.066, height=19, width=336)
        self.verify_code_status.configure(background="#d9d9d9")
        self.verify_code_status.configure(foreground="#000000")
        self.verify_code_status.configure(font="-family {Hack} -size 10")
        self.verify_code_status.configure(relief="flat")
        self.verify_code_status.configure(text="Kode Verify")

        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.009, rely=0.116, relheight=0.706, relwidth=0.453)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Diisi oleh Calon Peserta Didik''')

        self.tag_nama = ttk.Label(self.TLabelframe1)
        self.tag_nama.place(relx=0.042, rely=0.071, height=19, width=68, bordermode='ignore')
        self.tag_nama.configure(background="#d9d9d9")
        self.tag_nama.configure(foreground="#000000")
        self.tag_nama.configure(font="TkDefaultFont")
        self.tag_nama.configure(relief="flat")
        self.tag_nama.configure(text='''Nama Siswa''')

        self.name_field = ttk.Entry(self.TLabelframe1)
        self.name_field.place(relx=0.333, rely=0.071, relheight=0.049, relwidth=0.617, bordermode='ignore')
        self.name_field.configure(takefocus="")
        self.name_field.configure(cursor="ibeam")

        self.tag_jenisK = ttk.Label(self.TLabelframe1)
        self.tag_jenisK.place(relx=0.042, rely=0.141, height=19, width=75, bordermode='ignore')
        self.tag_jenisK.configure(background="#d9d9d9")
        self.tag_jenisK.configure(foreground="#000000")
        self.tag_jenisK.configure(font="TkDefaultFont")
        self.tag_jenisK.configure(relief="flat")
        self.tag_jenisK.configure(text='''Jenis Kelamin''')

        self.tag_tgllahir = ttk.Label(self.TLabelframe1)
        self.tag_tgllahir.place(relx=0.042, rely=0.212, height=19, width=76, bordermode='ignore')
        self.tag_tgllahir.configure(background="#d9d9d9")
        self.tag_tgllahir.configure(foreground="#000000")
        self.tag_tgllahir.configure(font="TkDefaultFont")
        self.tag_tgllahir.configure(relief="flat")
        self.tag_tgllahir.configure(text='''Tanggal Lahir''')

        self.tag_asalsklh = ttk.Label(self.TLabelframe1)
        self.tag_asalsklh.place(relx=0.042, rely=0.306, height=19, width=70, bordermode='ignore')
        self.tag_asalsklh.configure(background="#d9d9d9")
        self.tag_asalsklh.configure(foreground="#000000")
        self.tag_asalsklh.configure(font="TkDefaultFont")
        self.tag_asalsklh.configure(relief="flat")
        self.tag_asalsklh.configure(text='''Asal Sekolah''')

        self.tag_alamat = ttk.Label(self.TLabelframe1)
        self.tag_alamat.place(relx=0.042, rely=0.729, height=19, width=83, bordermode='ignore')
        self.tag_alamat.configure(background="#d9d9d9")
        self.tag_alamat.configure(foreground="#000000")
        self.tag_alamat.configure(font="TkDefaultFont")
        self.tag_alamat.configure(relief="flat")
        self.tag_alamat.configure(text='''Alamat Rumah''')

        self.jrk_field = ttk.Entry(self.TLabelframe1)
        self.jrk_field.place(relx=0.333, rely=0.447, relheight=0.049, relwidth=0.117, bordermode='ignore')
        self.jrk_field.configure(takefocus="")
        self.jrk_field.configure(cursor="ibeam")

        self.tag_jaraksekolah = ttk.Label(self.TLabelframe1)
        self.tag_jaraksekolah.place(relx=0.042, rely=0.447, height=19, width=89, bordermode='ignore')
        self.tag_jaraksekolah.configure(background="#d9d9d9")
        self.tag_jaraksekolah.configure(foreground="#000000")
        self.tag_jaraksekolah.configure(font="TkDefaultFont")
        self.tag_jaraksekolah.configure(relief="flat")
        self.tag_jaraksekolah.configure(text='''Jarak ke Sekolah''')

        self.tag_KM = ttk.Label(self.TLabelframe1)
        self.tag_KM.place(relx=0.458, rely=0.447, height=19, width=22, bordermode='ignore')
        self.tag_KM.configure(background="#d9d9d9")
        self.tag_KM.configure(foreground="#000000")
        self.tag_KM.configure(font="TkDefaultFont")
        self.tag_KM.configure(relief="flat")
        self.tag_KM.configure(text='''KM''')

        self.tag_tinggibdn = ttk.Label(self.TLabelframe1)
        self.tag_tinggibdn.place(relx=0.042, rely=0.518, height=19, width=74, bordermode='ignore')
        self.tag_tinggibdn.configure(background="#d9d9d9")
        self.tag_tinggibdn.configure(foreground="#000000")
        self.tag_tinggibdn.configure(font="TkDefaultFont")
        self.tag_tinggibdn.configure(relief="flat")
        self.tag_tinggibdn.configure(text='''Tinggi Badan''')

        self.tag_beratbdn = ttk.Label(self.TLabelframe1)
        self.tag_beratbdn.place(relx=0.042, rely=0.588, height=19, width=67, bordermode='ignore')
        self.tag_beratbdn.configure(background="#d9d9d9")
        self.tag_beratbdn.configure(foreground="#000000")
        self.tag_beratbdn.configure(font="TkDefaultFont")
        self.tag_beratbdn.configure(relief="flat")
        self.tag_beratbdn.configure(text='''Berat Badan''')

        self.tinggibdn_field = ttk.Entry(self.TLabelframe1)
        self.tinggibdn_field.place(relx=0.333, rely=0.518, relheight=0.049, relwidth=0.117, bordermode='ignore')
        self.tinggibdn_field.configure(takefocus="")
        self.tinggibdn_field.configure(cursor="ibeam")

        self.beratbdn_field = ttk.Entry(self.TLabelframe1)
        self.beratbdn_field.place(relx=0.333, rely=0.588, relheight=0.049, relwidth=0.117, bordermode='ignore')
        self.beratbdn_field.configure(takefocus="")
        self.beratbdn_field.configure(cursor="ibeam")

        self.tag_CM = ttk.Label(self.TLabelframe1)
        self.tag_CM.place(relx=0.458, rely=0.518, height=19, width=23, bordermode='ignore')
        self.tag_CM.configure(background="#d9d9d9")
        self.tag_CM.configure(foreground="#000000")
        self.tag_CM.configure(font="TkDefaultFont")
        self.tag_CM.configure(relief="flat")
        self.tag_CM.configure(text='''CM''')

        self.tag_KG = ttk.Label(self.TLabelframe1)
        self.tag_KG.place(relx=0.458, rely=0.588, height=19, width=19, bordermode='ignore')
        self.tag_KG.configure(background="#d9d9d9")
        self.tag_KG.configure(foreground="#000000")
        self.tag_KG.configure(font="TkDefaultFont")
        self.tag_KG.configure(relief="flat")
        self.tag_KG.configure(text='''KG''')

        self.tag_tpsklh = ttk.Label(self.TLabelframe1)
        self.tag_tpsklh.place(relx=0.042, rely=0.659, height=19, width=128, bordermode='ignore')
        self.tag_tpsklh.configure(background="#d9d9d9")
        self.tag_tpsklh.configure(foreground="#000000")
        self.tag_tpsklh.configure(font="TkDefaultFont")
        self.tag_tpsklh.configure(relief="flat")
        self.tag_tpsklh.configure(text='''Transportasi ke Sekolah''')

        self.style.map('TRadiobutton',background=[('selected', _bgcolor), ('active', _ana2color)])
        self.mtr_radio = ttk.Radiobutton(self.TLabelframe1)
        self.mtr_radio.place(relx=0.333, rely=0.659, relwidth=0.117, relheight=0.0, height=21, bordermode='ignore')
        self.mtr_radio.configure(value="Motor",variable=self.tp)
        self.mtr_radio.configure(text='''Motor''')

        self.angkot_radio = ttk.Radiobutton(self.TLabelframe1)
        self.angkot_radio.place(relx=0.479, rely=0.659, relwidth=0.24, relheight=0.0, height=21, bordermode='ignore')
        self.angkot_radio.configure(value="Transportasi Umum",variable=self.tp)
        self.angkot_radio.configure(text='''Angkutan Umum''')

        self.jalan_radio = ttk.Radiobutton(self.TLabelframe1)
        self.jalan_radio.place(relx=0.75, rely=0.659, relwidth=0.154, relheight=0.0, height=21, bordermode='ignore')
        self.jalan_radio.configure(value="Jalan Kaki",variable=self.tp)
        self.jalan_radio.configure(text='''Jalan Kaki''')

        self.tgl_cb = ttk.Combobox(self.TLabelframe1)
        self.tgl_cb.place(relx=0.333, rely=0.212, relheight=0.049, relwidth=0.11, bordermode='ignore')
        self.tgl_cb.configure(textvariable=self.tgl)
        self.tgl_cb['values'] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        self.tgl_cb.configure(takefocus="")

        self.bln_cb = ttk.Combobox(self.TLabelframe1)
        self.bln_cb.place(relx=0.458, rely=0.212, relheight=0.049, relwidth=0.298, bordermode='ignore')
        self.bln_cb.configure(textvariable=self.bln)
        self.bln_cb['values'] = ("Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","November","Desember")
        self.bln_cb.configure(takefocus="")

        self.thn_cb = ttk.Combobox(self.TLabelframe1)
        self.thn_cb.place(relx=0.771, rely=0.212, relheight=0.049, relwidth=0.173, bordermode='ignore')
        self.thn_cb.configure(textvariable=self.thn)
        self.thn_cb['values'] = ("1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010")
        self.thn_cb.configure(takefocus="")

        self.TLabelframe2 = ttk.Labelframe(top)
        self.TLabelframe2.place(relx=0.491, rely=0.116, relheight=0.457, relwidth=0.5)
        self.TLabelframe2.configure(relief='')
        self.TLabelframe2.configure(text='''Diisi oleh Orang Tua Calon Peserta Didik''')

        self.tag_ayah = ttk.Label(self.TLabelframe2)
        self.tag_ayah.place(relx=0.057, rely=0.109, height=19, width=66, bordermode='ignore')
        self.tag_ayah.configure(background="#d9d9d9")
        self.tag_ayah.configure(foreground="#000000")
        self.tag_ayah.configure(font="TkDefaultFont")
        self.tag_ayah.configure(relief="flat")
        self.tag_ayah.configure(text='''Nama Ayah''')

        self.tag_ibu = ttk.Label(self.TLabelframe2)
        self.tag_ibu.place(relx=0.057, rely=0.218, height=19, width=56, bordermode='ignore')
        self.tag_ibu.configure(background="#d9d9d9")
        self.tag_ibu.configure(foreground="#000000")
        self.tag_ibu.configure(font="TkDefaultFont")
        self.tag_ibu.configure(relief="flat")
        self.tag_ibu.configure(text='''Nama Ibu''')

        self.tag_kerjaibu = ttk.Label(self.TLabelframe2)
        self.tag_kerjaibu.place(relx=0.057, rely=0.436, height=19, width=122, bordermode='ignore')
        self.tag_kerjaibu.configure(background="#d9d9d9")
        self.tag_kerjaibu.configure(foreground="#000000")
        self.tag_kerjaibu.configure(font="TkDefaultFont")
        self.tag_kerjaibu.configure(relief="flat")
        self.tag_kerjaibu.configure(text='''Profesi / Pekerjaan Ibu''')

        self.tag_kerjaayah = ttk.Label(self.TLabelframe2)
        self.tag_kerjaayah.place(relx=0.057, rely=0.327, height=19, width=132, bordermode='ignore')
        self.tag_kerjaayah.configure(background="#d9d9d9")
        self.tag_kerjaayah.configure(foreground="#000000")
        self.tag_kerjaayah.configure(font="TkDefaultFont")
        self.tag_kerjaayah.configure(relief="flat")
        self.tag_kerjaayah.configure(text='''Profesi / Pekerjaan Ayah''')

        self.dadname_field = ttk.Entry(self.TLabelframe2)
        self.dadname_field.place(relx=0.358, rely=0.109, relheight=0.076, relwidth=0.596, bordermode='ignore')
        self.dadname_field.configure(takefocus="")
        self.dadname_field.configure(cursor="ibeam")

        self.momname_field = ttk.Entry(self.TLabelframe2)
        self.momname_field.place(relx=0.358, rely=0.218, relheight=0.076, relwidth=0.596, bordermode='ignore')
        self.momname_field.configure(takefocus="")
        self.momname_field.configure(cursor="ibeam")

        self.dadwork_field = ttk.Entry(self.TLabelframe2)
        self.dadwork_field.place(relx=0.358, rely=0.327, relheight=0.076, relwidth=0.596, bordermode='ignore')
        self.dadwork_field.configure(takefocus="")
        self.dadwork_field.configure(cursor="ibeam")

        self.momwork_field = ttk.Entry(self.TLabelframe2)
        self.momwork_field.place(relx=0.358, rely=0.436, relheight=0.076, relwidth=0.596, bordermode='ignore')
        self.momwork_field.configure(takefocus="")
        self.momwork_field.configure(cursor="ibeam")

        self.tag_eduayah = ttk.Label(self.TLabelframe2)
        self.tag_eduayah.place(relx=0.057, rely=0.545, height=19, width=139, bordermode='ignore')
        self.tag_eduayah.configure(background="#d9d9d9")
        self.tag_eduayah.configure(foreground="#000000")
        self.tag_eduayah.configure(font="TkDefaultFont")
        self.tag_eduayah.configure(relief="flat")
        self.tag_eduayah.configure(text='''Pendidikan Terakhir Ayah''')

        self.tag_eduibu = ttk.Label(self.TLabelframe2)
        self.tag_eduibu.place(relx=0.057, rely=0.655, height=19, width=129, bordermode='ignore')
        self.tag_eduibu.configure(background="#d9d9d9")
        self.tag_eduibu.configure(foreground="#000000")
        self.tag_eduibu.configure(font="TkDefaultFont")
        self.tag_eduibu.configure(relief="flat")
        self.tag_eduibu.configure(text='''Pendidikan Terakhir Ibu''')

        self.dadedu_field = ttk.Entry(self.TLabelframe2)
        self.dadedu_field.place(relx=0.358, rely=0.545, relheight=0.076, relwidth=0.596, bordermode='ignore')
        self.dadedu_field.configure(takefocus="")
        self.dadedu_field.configure(cursor="ibeam")

        self.momedu_field = ttk.Entry(self.TLabelframe2)
        self.momedu_field.place(relx=0.358, rely=0.655, relheight=0.076, relwidth=0.596, bordermode='ignore')
        self.momedu_field.configure(takefocus="")
        self.momedu_field.configure(cursor="ibeam")

        self.phnumdad_field = ttk.Entry(self.TLabelframe2)
        self.phnumdad_field.place(relx=0.472, rely=0.764, relheight=0.076, relwidth=0.483, bordermode='ignore')
        self.phnumdad_field.configure(takefocus="")
        self.phnumdad_field.configure(cursor="ibeam")

        self.phnummom_field = ttk.Entry(self.TLabelframe2)
        self.phnummom_field.place(relx=0.472, rely=0.873, relheight=0.076, relwidth=0.483, bordermode='ignore')
        self.phnummom_field.configure(takefocus="")
        self.phnummom_field.configure(cursor="ibeam")

        self.tag_noayah = ttk.Label(self.TLabelframe2)
        self.tag_noayah.place(relx=0.057, rely=0.764, height=19, width=123, bordermode='ignore')
        self.tag_noayah.configure(background="#d9d9d9")
        self.tag_noayah.configure(foreground="#000000")
        self.tag_noayah.configure(font="TkDefaultFont")
        self.tag_noayah.configure(relief="flat")
        self.tag_noayah.configure(text='''No Telepon Ayah''')

        self.tag_noibu = ttk.Label(self.TLabelframe2)
        self.tag_noibu.place(relx=0.057, rely=0.873, height=19, width=86, bordermode='ignore')
        self.tag_noibu.configure(background="#d9d9d9")
        self.tag_noibu.configure(foreground="#000000")
        self.tag_noibu.configure(font="TkDefaultFont")
        self.tag_noibu.configure(relief="flat")
        self.tag_noibu.configure(text='''No Telepon Ibu''')

        self.tag_62 = ttk.Label(self.TLabelframe2)
        self.tag_62.place(relx=0.415, rely=0.764, height=19, width=24, bordermode='ignore')
        self.tag_62.configure(background="#d9d9d9")
        self.tag_62.configure(foreground="#000000")
        self.tag_62.configure(font="TkDefaultFont")
        self.tag_62.configure(relief="flat")
        self.tag_62.configure(text='''+62''')

        self.tag_622 = ttk.Label(self.TLabelframe2)
        self.tag_622.place(relx=0.415, rely=0.873, height=19, width=24, bordermode='ignore')
        self.tag_622.configure(background="#d9d9d9")
        self.tag_622.configure(foreground="#000000")
        self.tag_622.configure(font="TkDefaultFont")
        self.tag_622.configure(relief="flat")
        self.tag_622.configure(text='''+62''')

        self.smp_name_field = ttk.Entry(top)
        self.smp_name_field.place(relx=0.16, rely=0.365, relheight=0.035, relwidth=0.279)
        self.smp_name_field.configure(takefocus="")
        self.smp_name_field.configure(cursor="ibeam")

        self.jk_boy = ttk.Radiobutton(top)
        self.jk_boy.place(relx=0.16, rely=0.216, relwidth=0.081, relheight=0.0, height=21)
        self.jk_boy.configure(text='''Laki - Laki''',value="Laki - Laki",variable=self.jk)

        self.jk_girl = ttk.Radiobutton(top)
        self.jk_girl.place(relx=0.245, rely=0.216, relwidth=0.089, relheight=0.0, height=21)
        self.jk_girl.configure(text='''Perempuan''',value="Perempuan",variable=self.jk)
        self.jk_girl.configure(compound='top')

        self.smp_radio = ttk.Radiobutton(top)
        self.smp_radio.place(relx=0.16, rely=0.316, relwidth=0.044, relheight=0.0, height=21)
        self.smp_radio.configure(text='''SMP''',value="SMP",variable=self.school)
        self.smp_radio.configure(compound='top')

        self.mts_radio = ttk.Radiobutton(top)
        self.mts_radio.place(relx=0.226, rely=0.316, relwidth=0.044, relheight=0.0, height=21)
        self.mts_radio.configure(text='''MTS''',value="MTS",variable=self.school)
        self.mts_radio.configure(compound='top')

        self.othersmp_radio = ttk.Radiobutton(top)
        self.othersmp_radio.place(relx=0.292, rely=0.316, relwidth=0.06, relheight=0.0, height=21)
        self.othersmp_radio.configure(text='''Lainnya''',value="Sekolah",variable=self.school)
        self.othersmp_radio.configure(compound='top')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.address_field = ttk.Entry(top)
        self.address_field.place(relx=0.16, rely=0.631, relheight=0.035, relwidth=0.279)
        self.address_field.configure(takefocus="")
        self.address_field.configure(cursor="ibeam")

        self.regist_button = ttk.Button(top)
        self.regist_button.place(relx=0.877, rely=0.897, height=45, width=116)
        self.regist_button.configure(takefocus="")
        # Change command to self.printVar to debug the Radio button
        # Channe command to self.checkTgl to debug the Combo Box
        self.regist_button.configure(command=self.insert_to_db)
        self.regist_button.configure(text='''Daftar''')

        self.tag_copyright = tk.Message(top)
        self.tag_copyright.place(relx=0.009, rely=0.914, relheight=0.088, relwidth=0.139)
        self.tag_copyright.configure(background="#d9d9d9")
        self.tag_copyright.configure(foreground="#000000")
        self.tag_copyright.configure(highlightbackground="#d9d9d9")
        self.tag_copyright.configure(highlightcolor="black")
        self.tag_copyright.configure(text='''Copyright 2019 © Reserved
SMK Cyber Media Utama''')
        self.tag_copyright.configure(width=147)

        self.tag_haraplampirkan = tk.Message(top)
        self.tag_haraplampirkan.place(relx=0.481, rely=0.598, relheight=0.204, relwidth=0.274)
        self.tag_haraplampirkan.configure(background="#d9d9d9")
        self.tag_haraplampirkan.configure(foreground="#000000")
        self.tag_haraplampirkan.configure(highlightbackground="#d9d9d9")
        self.tag_haraplampirkan.configure(highlightcolor="black")
        self.tag_haraplampirkan.configure(text='''Harap Lampirkan juga data offline sebagai berikut :

1. Ijazah SMP/MTS/Sederajat & SKHUN
2. Fotocopy Kartu Keluarga
3. Fotocopy Akta Kelahiran Calon Peserta Didik
4. Fotocopy KTP Orang Tua
5. Pas Foto 3X4cm & 2X3cm = 2 Lembar@ukuran
6. Kartu Indonesia Pintar (Opsional)''')
        self.tag_haraplampirkan.configure(width=290)
    def insert_to_db(self):
        student_name = self.name_field.get()
        student_jk = self.jk.get()

    # =======  Functions for Combo Box Debugging  ==========
    # ==== Don't activate if not want to Debug ComboBox ====
    # def checkTgl(self):
    #     akrip = self.tgl.get()
    #     print("Tanggal lahir =",akrip)
    #     self.checkBln()
    # def checkBln(self):
    #     bkrip = self.bln.get()
    #     print("Bulan lahir =",bkrip)
    #     self.checkThn()
    # def checkThn(self):
    #     ckrip = self.thn.get()
    #     print("Tahun lahir =",ckrip)
    #     print("=" * 25)

    # =======  Functions for Radio Button Debugging  =======
    # ===== Don't activate if not want to Debug Radio ======
    # def printVar(self):
    #     askrip = self.jk.get()
    #     print("Gender anda adalah",askrip)
    #     self.printVir()
    # def printVir(self):
    #     bskrip = self.school.get()
    #     print("Anda berasal dari",bskrip)
    #     self.printVur()
    # def printVur(self):
    #     cskrip = self.tp.get()
    #     print("Anda menggunakan",cskrip)
    #     print("=" * 25)
if __name__ == '__main__':
    vp_start_gui()