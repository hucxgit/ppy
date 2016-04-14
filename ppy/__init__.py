from flask import Flask
#from .Views import initView

def registerblueprint(app):
    from ad import ad as ad_blueprint
    from find import find as find_blueprint
    from Report import report as report_blueprint
    from login import login as login_blueprint
    from index import index as index_blueprint
    app.register_blueprint(ad_blueprint)
    app.register_blueprint(find_blueprint)
    app.register_blueprint(report_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(index_blueprint)



def create_app():
    app = Flask(__name__)
    registerblueprint(app)

    #initView(app)

    return app





    # /*
    # @app.route('/submit',methods=['GET', 'POST'])
    # def submit():
    #    print("1")
    #    name = None
    #    form = MyForm()
    #    print("2")
    #    if form.validate_on_submit():
    #        print("redirect")
    #        return redirect(url_for('success'))
    #    print("normal")
    #    return render_template('submit.html', form=form)
    # # jinjia2
    # @app.route('/test/jinjia')
    # def testjijia():
    #     # return  "testjijia"
    #     env = Environment(loader=PackageLoader('__main__', 'templates'))
    #     env.comment_start_string = '{##';
    #     env.comment_end_string = '##}'
    #     template = env.get_template('test0327_1.html')
    #     return template.render(the='hello', go='world')



    # @app.route('/success', methods=('GET', 'POST'))
    # def success():
    #     return "success hello world"
    #
    #
    #
    #
    # @app.route('/getUser')
    # def getUser():
    #     u = models.User(1, "hucx", 27)
    #     d = utils.MyEncoder().encode(u)
    #     return d
    #
    #
    #
    # # for test do not care
    # @app.route('/getUsers')
    # def getUsers():
    #     request = urllib2.Request("http://127.0.0.1:5001")
    #     print(request)
    #     response = urllib2.urlopen(request)
    #     print(response)
    #     return response.read()

    # @app.route('/test')
    # def test():
    #     template = Template('Hello !')
    #     return template.render()
    #
    #
    # @app.route('/test/<name>')
    # def testWithname(name=None):
    #     template = Template('Hello {{name}}!')
    #     return template.render(name="hucx")