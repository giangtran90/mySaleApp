function addToCart(id,name,price){
    // Ngan no chuyen trang
    event.preventDefault();
    // alert("Hello");
    // ham windows tich hop san de gui request len server bang js
    fetch('/api/add-cart', {
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'name': name,
            'price': price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok){
            throw new Error('Network response was not ok')
        }
        //console.log(response)
        return response.json()
    })
    .then(data => {
        //console.log(data)
        let counter = document.getElementById('cartCounter')
        //console.log(counter)
        counter.innerText = data.total_quantity
    })
    .catch(error => console.error('Lỗi:', error))
}

function pay() {
    if (confirm('Ban muon thanh toan khong?') == true){
        fetch('/api/pay', {
            method: 'post'
        })
        .then(response => response.json())
        .then(data => {
            if (data.code == 200){
                location.reload()
            }
        })
        .catch(error => console.error('Lỗi:', error))
    }
}