import graphene
from graphene_django import DjangoObjectType
from .models import Product



class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "nom", "description")
            


class Query(graphene.ObjectType):

    all_products = graphene.List(ProductType)

    def resolve_all_products(root, info):
        return Product.objects.all()

class ProductMutation(graphene.Mutation):
    class Arguments:
        nom = graphene.String(required=True)
        description = graphene.String(required=True)
        #image = Upload(required=False, description="Image for the product.",)
       # image = Upload(required=True)
   # success = graphene.Boolean()


    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls,root,info,**prod_data):
        #success = upload_file(image) 
        #return FileUpload(success=success)
        product=Product(
            nom=prod_data.get('nom'),
            description=prod_data.get('description')
        )
        product.save()
        return ProductMutation(product=product)
  




class UpdateProduct(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
        nom=graphene.String()
        description=graphene.String()
    product = graphene.Field(ProductType)

    @classmethod
    def mutate(cls,root,info,id,nom,description):
        product = Product.objects.get(id=id)
        product.nom = nom
        product.description = description
        product.save()
        return UpdateProduct(product=product)

class DeleteProduct(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    product = graphene.Field(ProductType)
    @classmethod
    def mutate(cls, root, info, id):
        product = Product.objects.get(id=id)
        product.delete()
        return 

class Mutation(graphene.ObjectType):
    add_products = ProductMutation.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()
   # file_upload = FileUpload.Field ()

schema = graphene.Schema(query=Query, mutation=Mutation)
