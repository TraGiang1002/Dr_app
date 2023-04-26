from website import create_app

app = create_app()
if __name__ == '__main__': #kiểm tra xem module đang được chạy có là file main không
    app.run(debug=True)