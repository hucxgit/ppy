import  os
def load_config():
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            print "load PRODUCTION"
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'DEVELOPMENT':
            print "load DEVELOPMENT"
            from development import DevelopmentConfig
            return DevelopmentConfig
        else:
            print "load PRODUCTION"
            from .production import ProductionConfig
            return ProductionConfig
    except ImportError, e:
        print "load DEVELOPMENT EXCEPTION"
        from default import Config
        return Config