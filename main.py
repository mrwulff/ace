import ast
import json
#import mechanize
#import requests
#import urllib2
#import urllib.request
#from urllib.request import urlopen
from datetime import date

from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from os.path import join
import mechanize
#from kivy.network.urlrequest import UrlRequest
#from pyobjus import autoclass
#NSString = autoclass('NSString')
#from pyobjus.dylib_manager import load_dylib, make_dylib






#print (mechanize3)


import pyrebase
#filename=''

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)



class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
        self._popup.open()

    def load_list(self, path, filename):
        pass

    def dismiss_popup(self):
        self._popup.dismiss()
    def img(self,a,b):
        #print a,b#
        global filename 
        filename=str(a)+str(b)
        #self.lbl.text=str(str(a)+str(b))

    class LoadDialogApp(App):
        pass





def loaddict():
    #print 'FROM CACHE'
    live=False
    zzr=open('mcache.txt','r')
    for line in zzr.readlines():
        zz=line
    zz=str.replace(zz,'OrderedDict','')
    #print zz
    zz=ast.literal_eval(zz)
    #print type(zz)
        
    #print len(zz)
    #print "WTF YOU GODAMN MORAN"
    return zz
        #for i in range(len(zz)):
        #    print zz[i]
        #    print type(zz[i])
        #    print zz[i][1]
        #    print type(zz[i][1])




def pyre(data,database):
    #print data
    config = {
      
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    auth = firebase.auth()

    user = auth.sign_in_with_email_and_password('kevincwulff@gmail.com','')
    #results=db.child("ACE").child(database).set(data)
    results = db.child(database).push(data, user['idToken'])
    #print results

    #firebase = pyrebase.initialize_app(config)
    #print firebase
    #db = firebase.database()
    #auth = firebase.auth()

def pyredl(database):
    #print data
    config = {

      }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    auth = firebase.auth()

    user = auth.sign_in_with_email_and_password('kevincwulff@gmail.com','')
    users = db.child(database).get()
    #rint users
    #results=db.child("ACE").child(database).set(data)
    #results = db.child(database).push(data, user['idToken'])
    #print results

    #firebase = pyrebase.initialize_app(config)
    #print firebase
    #db = firebase.database()
    #auth = firebase.auth()
    return users






class FirstScreen(Screen):
    pass

class IScreen(Screen):
    pass
    #print 'iscreen'




class SettingsScreen(Screen):
    pass
    
    def getdate(self,msg):

        
        today = date.today()

        #print dir(self.ids.items)
        self.lbl.text=str(today)

    def calculate(self, mid,mactype,mdate,mattype,ndue,emp):




        me=Object()
        me.machine_id=mid
        me.machine_type=mactype
        me.current_date=mdate
        me.m_type=mattype
        me.newdate=ndue
        me.employee_id=emp
        data= me.toJSON()
        #data=json.parse(data)


        data=json.loads(data)
        

        try:
            work=pyre(data,'machines')
        except:
            print ("Failed")
    load = ObjectProperty(None)
    #print load, "LOAD                   LOAD"
    cancel = ObjectProperty(None)

    def show_load_list(self):
        content = LoadDialog(load=self.load_list, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load a file list", content=content, size_hint=(1, 1))
        self._popup.open()

    def load_list(self, path, filename):
        pass
    def dismiss_popup(self):
            self._popup.dismiss()
    def img(self,a,b):
        pass
        #print a,b

        


class MScreen(Screen):

    def getdate(self,msg):

        
        today = date.today()

        #print dir(self.ids.items)
        self.lbl.text=str(today)


    def calculate(self, mid,mactype,mdate,mattype,ndue,emp):




        me=Object()
        me.machine_id=mid
        me.machine_type=mactype
        me.current_date=mdate
        me.m_type=mattype
        me.newdate=ndue
        me.employee_id=emp
        data= me.toJSON()
        #data=json.parse(data)


        data=json.loads(data)
        

        try:
            print ('omg')
            work=pyre(data,'maintenance')
            print ('fart')
        except:
            work = pyre(data, 'maintenance')
            print ("Failed")
        

class TestApp(App):
    pass


class HScreen(Screen):
    def pp(self,a,b):

        print (a)

    def pp2(self,req, result):
        for key, value in result['headers'].items():
            print('{}: {}'.format(key, value))
        print (result)
        #b=open('temp.txt','w')
        #b.write(str(result))
        #b.close()
        print
        #NSString.alloc()
    def loadd(self, a):
        print(a)
        print (a)
        '''
        #urllib.request.urlretrieve('https://google.com'verify=False,'temp.txt')
        #open / Applications / Python\ 3.7 / Install\ Certificates.command
        #html = urllib.request.get("http://en.wikipedia.org" , verify=False).text
        #html = urlopen("https://woot.com")
        #print(html)
        url='https://google.com'
        #req = UrlRequest('https://httpbin.org/headers', on_success=self.pp2,verify=False)
        #print (dir(NSString))
        #urllib2Wrapper = autoclass('urllib2Wrapper')
        #ulib2 = urllib2Wrapper.alloc().init()

        #NSString = autoclass('NSString')

        #ns = lambda x: NSString.alloc().initWithUTF8String_(x)
        #print (ns)

        #ulib2.openWithUrl_withMethod_withFile_(ns(self.params["--url"]), ns("GET"), ns(""))

        #ulib2.download()
        '''

        '''
        config.setdefaults('section1', {
                'key1': 'value1',
                'key2': '42'
        })
        '''
        print('here\'s our stor3age:', App.get_running_app().storage())
        c=App.get_running_app().storage()
        print (dir(c))
        b=open(str(c)+'test.txt','w')
        b.write('fuck')


        #.get_application
        print ((a),'omg')
        print (type(a))
        #b=open(a,'w')
        #b.write('HELLO\nWorld\nThisiskevin')
        #b.close()

        b=open(str(c)+'test.txt','r')
        for line in b.readlines():
            print (line)

    def loadd2(self,a):
        zz=''
        #print a
        
        if a=='web':
            #print 'FROM WEB'
            live=True
            users=pyredl('maintenance')
            zz=(users.val())
            #print type(zz)
            zzw=open('mcache.txt','w')
            zzw.write(str(zz))
            zzw.close()

        if a=='cache':
            #print 'FROM CACHE'
            live=False
            zzr=open('mcache.txt','r')
            for line in zzr.readlines():
                zz=line
            #print zz,abs
            zz=replace(zz,'OrderedDict','')
            #print zz

            zz=ast.literal_eval(zz)
            #print type(zz)
        
            
            #for i in range(len(zz)):
            #    print zz[i]
            #    print type(zz[i])
            #    print zz[i][1]
            #    print type(zz[i][1])
            #    print
        #print(zz.key()) # users

class CustomScreen(Screen):
    hue = NumericProperty(0)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableLabel.old(RecycleDataViewBehavior, GridLayout,Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(True)
    selectable = BooleanProperty(True)
    cols = 6

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        #print index
        self.label1_text = data['label1']['text']
        self.label2_text = data['label2']['text']
        self.label3_text = data['label3']['text']
        self.label4_text = data['label4']['text']
        self.label5_text = data['label5']['text']
        self.label6_text = data['label6']['text']
        #self.label2_text = data['label2']['text']
        #self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            popup = Popup(title='Test popup',
                          content=Label(text='Hello world'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            #pass
            #print("selection changed to {0}".format(rv.data[index]))
        else:
            pass
            #print("selection removed for {0}".format(rv.data[index]))




class SelectableLabel2(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        #print index,'WTF MAN'
        self.label1_text = str(index)
        #self.label2_text = data['label2']['text']
        #self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
            popup = Popup(title='Test popup',
                          content=Label(text='Hello world'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
        else:
            pass
            #print("selection removed for {0}".format(rv.data[index]))

items_1 = {'apple', 'banana', 'pear', 'pineapple'}
items_2 = {'dog', 'cat', 'rat', 'bat'}


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 3

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        self.label1_text = str(index)
        self.label2_text = data['label2']['text']
        self.ids['id_label3'].text = data['label3']['text']  # As an alternate method of assignment
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))



class RVold(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        
        dd=[]
        el=[]
        ml=[]
        cl=[]
        tl=[]
        dl=[]
        il=[]
        
        zz=loaddict()
        for y in range(len(zz)):
            e=zz[y][1]['employee_id']
            el.append(e)
            m=zz[y][1]['m_type']
            ml.append(m)
            c=zz[y][1]['current_date']
            cl.append(c)
            t=zz[y][1]['machine_type']
            tl.append(t)
            d=zz[y][1]['newdate']
            dl.append(d)
            i=zz[y][1]['machine_id']
            il.append(i)
            nn=str(e+m+c+t+d+i)
            dd.append(nn)
        #paired_iter = zip(e,t,c,m,d,i)
        #paired_iter = zip(il,ml,cl,tl,dl,el)
        paired_iter = zip(il,tl,cl,ml,dl,el)
#month (EOM)

        #print paired_iter
        self.date=[]
        for i1,i2,i3,i4,i5,i6 in paired_iter:
        #for i1,i2 in paired_iter:
            d={'label1': {'text': i1}, 'label3': {'text': i3}, 'label2': {'text': i2}, 'label4': {'text': i4}, 'label5': {'text': i5}, 'label6': {'text': i6}}
            #d={'label1': {'text': i1}, 'label2': {'text': i2}}
            #print d
            self.data.append(d)


        #self.data = [{'text': str(zz[x][1])} for x in range(len(zz))]
        #self.data = [{'text': str(dd[x])} for x in range(len(zz))]

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        paired_iter = zip(items_1, items_2)
        self.data = []
        for i1, i2 in paired_iter:
            d = {'label2': {'text': i1}, 'label3': {'text': i2}}
            self.data.append(d)
        # can also be performed in a complicated one liner for those who like it tricky
        # self.data = [{'label2': {'text': i1}, 'label3': {'text': i2}} for i1, i2 in zip(items_1, items_2)]




        


class RVScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass
    '''
    pass

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(self.screen_switch_one, 2)

    def screen_switch_one(self, dt):
        self.current = '_first_screen_'
        #Clock.schedule_once(self.screen_switch_two, 2)

    def screen_switch_two(self, dt):
        self.current = '_second_screen_'
        #self.ids.first_screen.ids.first_screen_label.text = "Hi I'm The Fifth Screen"
        #Clock.schedule_once(self.screen_switch_three, 2)

    def screen_switch_three(self, dt):
        self.current = '_third_screen_'
        #Clock.schedule_once(self.screen_switch_four, 2)

    def screen_switch_four(self, dt):
        self.current = '_fourth_screen_'
        #Clock.schedule_once(self.screen_switch_one, 2)
        '''


class SwitchingScreenApp(App):
    '''
    def build_config(self, config):
        config.setdefaults('section1', {
            'key1': 'value1',
            'key2': '42'
        })
    '''
    def storage(self):
        return self.user_data_dir

    def build(self):
        #a=self.get_application_config()
        #self.get_application
        #print ((a),'omg')
        #print (type(a))
        #b=open(a,'w')
        #b.write('omg')
        #b.close()

        return MyScreenManager()



if __name__ == "__main__":
    SwitchingScreenApp().run()
