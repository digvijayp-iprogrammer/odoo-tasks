{
    'name':"College ERP",
    'version':"19.2.1.1",
    'license':'LGPL-3',
    'summary':"An ERP For College Education",
    'description':"""From Student Administration to exam , it covers all
                  the all the aspects of college administration""",
    'author':'Digvijay',
    'category':'Education',
    'website':'https://www.sguk.ac.in',
    'maintainer':'SGU PVT LTD <INFO@SGU.COM>',
    'sequence':3,
    'data':["security/college_erp_security.xml",
        "security/ir.model.access.csv",
            "views/college_student_views.xml",
            "views/college_erp_menus.xml"],
    'application':True,
    'auto_install':True,
    'installable':True
}