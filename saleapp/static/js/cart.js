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

function deleteProductInCart(id){
    const formatter = new Intl.NumberFormat('vi-VN', {
      style: 'decimal',
      minimumFractionDigits: 1,
      maximumFractionDigits: 1
    });
    if (confirm("Ban co chac muon xoa san pham") == true){
        fetch('/api/delete-cart/' + id, {
            method: 'delete',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            let productId = document.getElementById('product-' + id)
            productId.style.display = "none"

            let counter = document.getElementsByClassName('cart-counter')
            for (let i=0; i < counter.length; i++){
                counter[i].innerText = data.total_quantity
            }

            let totalAmount = document.getElementById('total-amount')
            totalAmount.innerText = formatter.format(data.total_amount) + ` VND`
        })
        .catch(error => console.error('Lỗi:', error))
    }
}

function addComment(productId){
    let content = document.getElementById('commentId')
    console.log(content.value)
    if (content != null){
        fetch('/api/comment-product', {
            method: 'post',
            body: JSON.stringify({
                'content': content.value,
                'product_id': parseInt(productId)
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.status == 201){
                let c = data.comment
                let area = document.getElementById('commentArea')
                area.innerHTML = `
                    <div class="row">
                        <div class="col-md-1 col-xs-4">
                            <img src="${c.user.avatar}" class="img-fluid rounded-circle" width="50" alt="demo">
                        </div>
                        <div class="col-md-11 col-xs-8">
                            <p>${c.content}</p>
                            <p><em>${moment(c.created_date, "YYYY-MM-DD hh:mm:ss").locale('vi').fromNow()}</em></p>
                        </div>
                    </div>
                ` + area.innerHTML
            } else {
                alert(data.err_msg)
            }
        })
        .catch(error => console.error('Lỗi:', error))
    }
}