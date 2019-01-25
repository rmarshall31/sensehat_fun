# sensehat_fun
I have a rpi with a sense hat in my cube at work. The goal of this project is to have some neat things displayed on it.


## requirements
install python-sense-hat

```bash
sudo apt install python-sense-hat
```

## installation

```bash
sudo cp ~/projects/sensehat_fun/shfun.service /lib/systemd/system
sudo systemctl daemon-reload  # to load the service
sudo systemctl enable shfun  # to start on reboot
sudo systemctl start shfun  # to start now
```
