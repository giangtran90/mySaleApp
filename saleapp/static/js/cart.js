function addToCart(id,name,price){
    // Ngan no chuyen trang
    event.preventDefault();
    const formatter = new Intl.NumberFormat('vi-VN', {
      style: 'decimal',
      minimumFractionDigits: 1,
      maximumFractionDigits: 1
    });
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
        let counter = document.getElementsByClassName('cart-counter')
        //console.log(counter)
        for (let i = 0; i <= counter.length; i++)
            counter[i].innerText = data.total_quantity

        let totalAmount = document.getElementById('total-amount')
        totalAmount.innerText = formatter.format(data.total_amount) + ` VND`
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

function updateCart(id, obj){
    const formatter = new Intl.NumberFormat('vi-VN', {
      style: 'decimal',
      minimumFractionDigits: 1,
      maximumFractionDigits: 1
    });
    fetch('/api/update-cart', {
        method: 'put',
        body: JSON.stringify({
            'id': id,
            'quantity': parseInt(obj.value)
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        let counter = document.getElementsByClassName('cart-counter')
        for (let i=0; i < counter.length; i++){
            counter[i].innerText = data.total_quantity
        }
        let totalAmount = document.getElementById('total-amount')
        totalAmount.innerText = formatter.format(data.total_amount) + ` VND`
    })
    .catch(error => console.error('Lỗi:', error))
}