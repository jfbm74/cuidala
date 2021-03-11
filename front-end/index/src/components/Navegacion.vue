<template>
          <!-- Start Header Style -->
        <div id="header" class="header navegacion">
            <!-- Start Mainmenu Area -->
            <div id="sticky-header-with-topbar" class="mainmenu__menu__wrap bg-white sticky__header hidden-xs">
                <div class="mainmenu__menu__inner">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-3 col-lg-3 col-sm-12">
                                <div class="logo">
                                    <a href="index.html"><!--<img src="images/logo/best-care.png" alt="logo">--></a>
                                </div>
                            </div>
                            <div class="col-md-8 col-lg-8 col-sm-10">
                                <!-- Start Mainmenu -->
                                <nav class="mainmenu__nav">
                                    <ul class="main__menu">
                                        <li class="drop"><a><router-link to="/">Inicio</router-link></a>
                                            <ul class="dropdown">
                                                <li><a href="index-animation-text-1.html">animation text 1</a></li>
                                            </ul>
                                        </li>
                                        <!--<li><a href="gallery.html">gallery</a></li>-->
                                        <li><a href="about.html">Nosotros</a></li>
                                        <li class="drop"><a href="#">Cuidadores</a>
                                            <!--<ul class="dropdown">
                                                <li><a href="blog-list.html">blog list</a></li>
                                                <li><a href="blog-details.html">blog details</a></li>
                                                <li><a href="shop-grid.html">shop grid</a></li>
                                                <li><a href="shop-list.html">shop list</a></li>
                                                <li><a href="product-details.html">Product details</a></li>
                                                <li><a href="team.html">team</a></li>
                                                <li><a href="team-details.html">team details</a></li>
                                                <li><a href="service.html">service</a></li>
                                                <li><a href="cart.html">cart</a></li>
                                                <li><a href="wishlist.html">wishlist</a></li>
                                                <li><a href="appoinment.html">appoinment</a></li>
                                            </ul>-->
                                        </li>
                                        <!--<li class="drop"><a href="product-details.html">Tienda</a>
                                            <ul class="dropdown">
                                                <li><a href="shop-grid.html">shop grid</a></li>
                                                <li><a href="shop-list.html">shop list</a></li>
                                                <li><a href="product-details.html">Detalles de producto</a></li>
                                            </ul>
                                        </li>-->
                                        <li><a href="contact.html">Contacto</a></li>
                                        <li><a><router-link to="/login">sesión</router-link></a></li>
                                        <li><a class="registro"><router-link to="/registro">Registro</router-link></a></li>
                                    </ul>
                                </nav>
                                <!-- End Mainmenu -->
                            </div>
                            <div class="col-md-1 col-lg-1 col-sm-2">
                                <div >
                                    <ul class="cart__search__list">
                                        <li class="cart__menu"><!--<a href="#"><i class="zmdi zmdi-shopping-cart"></i></a>-->
                                            <!--<span class="badge--cart">2</span>-->
                                        </li>
                                    </ul>
                                </div>
                                <!-- Start Shopping basket -->
                                <div class="dropdown__shopping__basket">
                                    <div class="shopping__basket_notices">
                                        <em class="color main-font">Your Total item (02)</em>
                                        <span class="close icon-clear pull-right"><i class="zmdi zmdi-close"></i></span>
                                    </div>
                                    <div class="top-cart-content">
                                        <ul class="mini-products-list">
                                            <li>
                                                <a class="shopping-image" href="single-product.html">
                                                    <!--<img alt="images" src="images/product/sm-img/1.png">-->
                                                </a>
                                                <div class="shopping-product-details">
                                                    <p class="cartproduct-name">
                                                        <a href="single-product.html">Pellentesque habitant </a>
                                                    </p>
                                                    <strong class="qty">qty:1</strong>
                                                    <span class="sig-price">$222.00</span>                
                                                </div>
                                                <div class="shopping-pro-action">
                                                    <a class="btn-remove" href="#">remove</a>
                                                    <a class="btn-edit" href="#">edit</a>
                                                </div>
                                            </li>
                                            <!-- single item -->
                                            <li>
                                                <a class="shopping-image" href="single-product.html">
                                                    <!--<img alt="images" src="images/product/sm-img/1.png">-->
                                                </a>
                                                <div class="shopping-product-details">
                                                    <p class="cartproduct-name">
                                                        <a href="single-product.html">Pellentesque habitant </a>
                                                    </p>
                                                    <strong class="qty">qty:1</strong>
                                                    <span class="sig-price">$222.00</span>                
                                                </div>
                                                <div class="pro-action">
                                                    <a class="btn-remove" href="#">remove</a>
                                                    <a class="btn-edit" href="#">edit</a>
                                                </div>
                                            </li>
                                            <!-- single item -->
                                        </ul>
                                        <div class="top-subtotal">
                                            Subtotal: <span class="sig-price">$444.00</span>
                                        </div>
                                        <div class="cart-actions">
                                            <button class="cart-btn"><span>Checkout</span></button>
                                        </div>
                                    </div>                                            
                                </div>
                                <!-- End Shopping basket -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>-->
            <!-- End Mainmenu Area -->
            <!-- Mobile-menu-area start -->
            <div class="mobile-menu-area hidden-md hidden-lg hidden-sm">
                <div class="fluid-container mobile-menu-container">
                    <div class="mobile-logo"><a href="index.html"><!--<img src="images/logo/best-care.png" alt="Mobile logo">--></a></div>
                    <div class="mobile-menu clearfix">
                        <nav id="mobile_dropdown">
                            <ul>
                                <li><a><router-link to="/">home</router-link></a>
                                    <ul>
                                        <li><a href="index-animation-text-1.html">animation text 1</a></li>
                                    </ul>
                                </li>
                                <li><a href="about.html">about</a></li>
                                <li><a href="gallery.html">gallery</a></li>
                                <li><a href="#">pages</a>
                                    <ul>
                                        <li><a href="blog-list.html">blog list</a></li>
                                        <li><a href="blog-details.html">blog details</a></li>
                                        <li><a href="shop-grid.html">shop grid</a></li>
                                        <li><a href="shop-list.html">shop list</a></li>
                                        <li><a href="product-details.html">Product details</a></li>
                                        <li><a href="team.html">team</a></li>
                                        <li><a href="team-details.html">team details</a></li>
                                        <li><a href="service.html">service</a></li>
                                        <li><a href="cart.html">cart</a></li>
                                        <li><a href="wishlist.html">wishlist</a></li>
                                        <li><a href="appoinment.html">appoinment</a></li>
                                    </ul>
                                </li>
                                <li><a href="product-details.html">shop</a>
                                    <ul>
                                        <li><a href="shop-grid.html">shop grid</a></li>
                                        <li><a href="shop-list.html">shop list</a></li>
                                    </ul>
                                </li>
                                <li><a href="contact.html">contact us</a></li>
                            </ul>
                        </nav>
                    </div>  
                </div>
            </div>
            <!-- Mobile-menu-area End -->
        </div>
</template>

<script>
export default {
  name: 'Navegacion',
}
</script>
