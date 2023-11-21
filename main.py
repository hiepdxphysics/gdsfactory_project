import gdsfactory as gf
from gdsfactory.dft.siepic import add_fiber_array_siepic
from gdsfactory.components import spiral
from ubcpdk.components.grating_couplers import gc_te1550
from ubcpdk.components.cells import straight

add_fiber_array = gf.partial(
    add_fiber_array_siepic, gc_port_name="opt1", grating_coupler = "gc_te1550"
)

ring = gf.partial(mzi)

if __name__ == "__main__":
    print("Hello")

    # c = spiral(length=10e3, port_spacing=500, radius=20, direction="EAST")
    c = add_fiber_array(spiral)
    c.show()
    c.write_gds_with_metadata("demo.gds")