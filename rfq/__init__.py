from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import configure_mappers
from core.db import engine

# Reflect all existing tables (like supplier_supplier)
AutoBase = automap_base()
AutoBase.prepare(engine, reflect=True)

# Export the automapped Supplier model
Supplier = AutoBase.classes.supplier_supplier

# Let relationship assignment happen later (no circular imports here)
def bind_supplier_relationship(RFQ):
    RFQ.supplier.property.mapper.class_ = Supplier
    configure_mappers()
