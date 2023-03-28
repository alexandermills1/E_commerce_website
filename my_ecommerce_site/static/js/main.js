// # * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 *

// const addToCart = (id, quantity, m) => {
//     // Loop through the array of items and make a separate API call for each item
//     items.forEach((item) => {
//     const { id, quantity } = item;

//     // Send a PUT request to update the product quantity
//     axios.put(`/product/${id}/`, {
//         quantity: quantity - 1
//     })
//         .then((response) => {
//         if (response.data.success) {
//             // Check if the item is already in the cart
//             axios.get(`/cart-item/?title=${id}`)
//             .then((response) => {
//                 if (response.data.length > 0) {
//                 // Item already in the cart, update its quantity
//                 const cartItemId = response.data[0].id;
//                 const cartItemQuantity = response.data[0].quantity;
//                 axios.put(`/cart-item/${cartItemId}/`, {
//                     quantity: cartItemQuantity + 1
//                 })
//                     .then((response) => {
//                     // Redirect to the cart page
//                     window.location.href = '/cart/';
//                     })
//                     .catch((error) => {
//                     console.log(error);
//                     });
//                 } else {
//                 // Item not in the cart, create a new cart item with quantity 1
//                 axios.post('/cart-item/', {
//                     title: id,
//                     quantity: 1
//                 })
//                     .then((response) => {
//                     // Redirect to the cart page
//                     window.location.href = '/cart/';
//                     })
//                     .catch((error) => {
//                     console.log(error);
//                     });
//                 }
//             })
//             .catch((error) => {
//                 console.log(error);
//             });
//         }
//         })
//         .catch((error) => {
//         console.log(error);
//         });
//     });
// };
  
const addToCart = (productId) => {
    axios.post('/cart-item/', { product_id: productId })
      .catch((err) => {
        alert(err);
      })
      .then((response) => {
        if (response.data.success) {
          window.location.reload();
        }
      });
  }  


// # * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 *

const alterProductQuantity = (id, quantity, m) => {
    if ( m === "A" ){
        quantity++
    } else {
        quantity--
    }
    axios.put(`/product/${id}/`,{
        quantity : quantity
    })
    .catch((err) =>{
        alert(err)
    })
    .then((response) =>{
        if(response.data.success){
            window.location.reload()
        }
    })
}

const deleteProduct = (id) =>{    
    axios.delete(`/product/${id}/`)
    .catch((err) =>{
        alert(err)
    })
    .then((response) =>{
        if(response.data.success){
            window.location.reload()
        }
    })
}