import web
import json
from scrapfont import scrapdb
from scrapfont import filesystem

web.config.debug = False
urls = (
    '/', 'Index',
    '/upload', 'Upload',
    '/img/(.*)', 'Image',
    '/ransom', 'Ransom'
)

app = web.application(urls, globals(), autoreload=True)
db = web.database(dbn='sqlite', db='scrapfont.db')

render = web.template.render('templates/', base="base")

#------------------------------------------------------------------------------
class Index(object):
    def GET(self):
        return render.index()

#------------------------------------------------------------------------------
class Upload(object):
    def GET(self):
        return render.upload()

    def POST(self):
        x = web.input(myletter=None,myfile={})
        ext = x.myfile.filename.split('.')[-1]
        dirpath = 'img/' + x.myletter
        if 'myfile' in x:
            uid = str(scrapdb.add_letter(db, x.myletter, ext))
            filepath = filesystem.upload_file(dirpath, uid, ext, x.myfile.file)
            return render.upload(letter=x.myletter, imgpath= '/' + filepath)
        else:
            return render.upload(error="Choose a file.")

#------------------------------------------------------------------------------
class Image(object):
    def GET(self, name):
        ext = name.split('.')[-1]
        path = 'img/' + name
        cType = {
            "png":"image/png",
            "jpg":"image/jpg",
            "gif":"image/gif",
            "ico":"image/x-icon"
        }
        if filesystem.file_exists(path):
            web.header("Content-Type", cType[ext])
            return filesystem.open_image(path) 
        else:
            raise web.notfound()

#------------------------------------------------------------------------------
class Ransom(object):
    def GET(self):
        return render.ransomnote()

    def POST(self):
        x = web.input(inputchar=None)
        if x['inputchar']:
            if x['inputchar'].isalpha():
                result = scrapdb.get_random_letter_file(db,
                                                        x['inputchar'].lower())
                return json.dumps(result)
        else:
            raise web.notfound()

#------------------------------------------------------------------------------
if __name__ == "__main__":
        app.run()
