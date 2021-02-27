import graphene
from .models import User
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = User
        # if you want to restrict to only these fields
        # fields = ('id', 'email', 'password', 'username')


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.UUID(required=True))
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()

    def resolve_user(self, info, id):
        return User.objects.get(id=id)

    @login_required
    def resolve_me(self, info):
        user = info.context.user
        # Can  use @login_required decorator from django-graphql-jwt to restrict queries and mutations to authenticated users instead of manually handling like below.
        # if(user.is_anonymous):
        #     raise Exception('Not logged in!')
        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, password: str, email: str):
        user = User.objects.create_user(email=email, password=password)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
