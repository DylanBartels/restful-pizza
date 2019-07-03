from ..models import Pizza, Order, Customer, Specification


def get_dummy_order():
    order = Order.objects.create(
        status="creating",
        payment=True,
        customer=Customer.objects.create(
            name="Dylan Bartels",
            address="Kantstrasse 86",
            city="Berlin",
            zip_code="781644"
        )
    )
    Specification(
        order=order,
        pizza=Pizza.objects.create(flavor="margherita"),
        size="medium",
        quantity=30
    ).save()
    Specification(
        order=order,
        pizza=Pizza.objects.create(flavor="pepperoni"),
        size="large",
        quantity=7
    ).save()
    Specification(
        order=order,
        pizza=Pizza.objects.create(flavor="mozzarella"),
        size="small",
        quantity=3
    ).save()

    return order
