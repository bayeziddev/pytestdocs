from smartgen_docs.core import Builder

def build_new_site():
    print("Starting smartgen-docs build process...")
    # Initialize builder mapping to your config and output folder
    builder = Builder(config_path='smartgen.yml', site_dir='site')
    builder.build()
    print("Success! Documentation built in the 'site/' directory.")

if __name__ == '__main__':
    build_new_site()