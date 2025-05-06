FROM ubuntu:24.04

# Устанавливаем Python3 и pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем другие зависимости (если нужно)
# RUN apt-get install -y <other-packages>

# Указываем путь к Python3, чтобы он был доступен по /usr/bin/python3
RUN ln -s /usr/bin/python3 /usr/bin/python

# Указываем рабочую директорию (опционально)
WORKDIR /workspace

# Команда по умолчанию (если нужно)
CMD ["bash"]