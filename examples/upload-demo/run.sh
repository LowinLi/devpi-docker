set -e
source .env

echo "安装依赖..."
python -m pip install -r requirements.txt

echo "打包pip库..."
cp -r src ${PIP_NAME}
python setup.py sdist bdist_wheel

echo "打包自动文档..."
cd doc
make clean
sphinx-apidoc -o source ../${PIP_NAME}/
make html
cd ..
python -m zipfile -c dist/${PIP_NAME}-${PIP_VERSION}.doc.zip doc/build/html/*

echo "上传..."
devpi use http://0.0.0.0:7104
devpi login lowinli --password=password
devpi use http://0.0.0.0:7104/lowinli/devpi
devpi upload --with-docs dist/*
devpi logout

echo "清理本地..."
rm -r dist
rm -r ${PIP_NAME}
echo "完成"