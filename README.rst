MyProjects
==========

This app is (intended) for use on a personal website, to keep track of
projects -- it was created for http://jaredforsyth.com (example:
http://jaredforsyth.com/projects)

It describes two models::
    
    class Project(models.Model):
        title
        slug
        author : User
        short_desc
        description
        source : File (blank=True)
        url
        image : Image
        time : DateTime
        status : [ alpha, beta, released ]
        tags : tagging.TagField
        types

    class Type(models.Model):
        title
        slug

and that pretty much sums it up. I welcome any feedback =)
