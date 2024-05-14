<template>
  <div class="containertoRecommend">
    <div class="toRecommend-title">
      <p>Recommend For You</p>
    </div>
    <div class="toRecommend-container">
      <div class="leftside-container" @mouseover="expandLeft" @mouseleave="shrinkLeft">
        <svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="100" height="100" fill="url(#pattern0_141_5)"/>
        <defs>
        <pattern id="pattern0_141_5" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use xlink:href="#image0_141_5" transform="scale(0.0111111)"/>
        </pattern>
        <image id="image0_141_5" width="90" height="90" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAAER0lEQVR4nO2dXWsVRxiAn2j05CjWHyHilVgVLS0oarzQP6CUIv0FragotQhVb1uMxkg0/8GPJEbjTSm0tHjj98dPsK0xKRRL0wa3THkPyGHP7mQ5M/Pu7DzwQkjOnpl5Mvs1884uJBKJsKxI/wC3tIEx4A+Jy/K7RJ+5CGRdcSFZ7j+/5oj+LYnuP1mPSCTR9SRLPTqJjoos9egkOiqy1KOTaOesA76UO7RDwEBEPXoAOCx3pEelrUFYCzztavQtoOWovIUcyfOOyjJtmOwq64m02Ttf9OhhdxzJHsspa9RBOS1pQ17bTJu9M1qwO7uQ3QauAm8lxh2M3hVJzuQw4p3PCirksmcPODoXlEk28SmBBuCnAskOIXkq5KTDagvZs8AQeqlNG2x6wx1gFfpYZVl3NXuljeyv0ceZOkm2lf0L+rhfN8k2smcrfNde4DxwE3ghNyj/AIvy83P52zlgTwUxs3WUXCT7HXDAcvvtwITMdGfLDHP3eA3YZlnWQalb7SS/f5Ixx+SfpdccsNjGyLlXQW6vuAt8aCl7Vup6WulJuy+0gUvAUh8ld+JfYETDpVloNslgTeY4HgEbaSg7gN89SO7EG+ATGsZHwJ8eJXfClLmTBh0u5gJI7sTrJhxGhoCHASV34knsCZKXFEiOPkFym6NLuKqxZHmdXTvuKZDbHTNExnYFUvPC3H5vJSImFEjtFWbuMQpaFQeIfMW8zLLUnn0KZJbFbiLgvAKRZXGWCJhUILIsbviWsga4soxj6oJkEBXdZb1QILIsnnl28n8mUJWKmu16MadApM34hzcnJjnkr4pf+rYguWRRgciy+NunkyTan5PKu0nRRf+cgh4b4tBReCPUljXWebnIvS72RyM/GbYdOHHCLQUiy+I6EXBOgciy+IYI2KtAZFnsIpJBpQUFMotmx6MYVDKkYVKP01iZ0oH/6Kaz7ioQ2x3TRMhmyYXLlISpyxYiZUSB4E58S+QJNA8USH4cewINko71OqBkk1i5gYawM2CSo8libRQ7AqTtfkxD2ShJ4q4lP2jS4aLoBHnB0aWf+c7vYl5aMQicBH6Qm4Jhi222SC5c9yqpKvFOyjXX7mUMy2e/B05I3WsziDSTk7k5bLn9VpnVmK94HB5fxm31/pwM15k6LH8rWtA5vczvWi0ZRGcl7+KZTIstSszJE3Cuy2d2VRiFu92jrqrXGpYtUf4RffxUUF+Vsm0W3Z9CH1+V1FmVbNvHSAyij8G6PEaiNg8VqXMbVsoJTn1v6NNeOS1t9s7ngSSvIJzsIwTgimfJbQ8vUyiTbcr0znHPPfmip7WCRbJNm72zHniZcxxreXyZwitHZbVyzj8mte0DAmFkH5Nd+ojj58JlPcIVK6VNY9LGYJJ9k3kW3ViyJDqJjoos9egkOiqy1KOT6KjIUo/2w4LHlyk0mjFPL1NoPG0PL1NIeHiZQiKRwJb/AFk084MboAwLAAAAAElFTkSuQmCC"/>
        </defs>
        </svg>
        <p class="black-font">집중 잘되는 주말 오후!</p>
      </div>
      <div class="linkToRecommendButton" @click="navigateToForYouView">
        <svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="90" height="90" fill="url(#pattern0_142_7)"/>
        <defs>
        <pattern id="pattern0_142_7" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use xlink:href="#image0_142_7" transform="scale(0.0111111)"/>
        </pattern>
        <image id="image0_142_7" width="90" height="90" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFP0lEQVR4nO2dSYhdRRSGK86KIi46JiaKOKA4jwtFEcS4U1tBRU2CQ1pQ4xDaxgEEdw4LwVYXrl0pTZwWTlvRTbfB1oVkMokTGbqTiGKiiZ8c3gm8jvfeN52abt8PGppHv1un/lev6tSpU6eda2hoaGhoaGhoaGhoaOgO4EjgauAh4FXgA2Aa2ATMAvv1Z1Zfm9a/eUXfc5U8o8vm5hfAUuAp4GNgL4OzB/gIeBJY4uYzwPHACuAL4CD+OAB8DiwHjnPzBeBEHWm/EJ4dwIvAya6uAEcDY8AM8REbRsUmVyeA64HvSI8fgJtc7sicCLwF/Gsgyj4dhYuAxcDT+tqgiG3jwLEuR4BzgW+wY7SgDZmKrJgEznY5IV9HIzetnUUF7cjItkTcwhtdDgC3A38ZC0BFe9bIZuhulzLAw758Ylfepg+kDyMuRYBh3Rx4wZW3i0ex73IpIfOakQdQSkXbPpFp5GaXkHdhvfD9j4r2fbMnujcivicwFaCzVNgQgsmofrZuRoLgym0IxXhYdeduqy12fF1RYUcopK83hBb5KODbgJ0kAaHReE24QJTx1jcnoYU1IePJu+ax0LtEgxBCPxOhcyQkdGGAy0fY89cYPXNpCf2bHMX5FHplpI6RmNDCvT6FloPUKLj0hP7El8hLfAaNMhT6oJdUBs27iIZLT2hhtQ+hJbklGi5Nodf6SNPaHbNHLk2hd5umn2kuXFRcmkILV1oKvSp2b1y6Qj9gKbRkdUbFpSv0S5ZCfxi7Ny5doe0WxNAh0cyEXmcp9I/9pm+ZGVEC8dnsrOgjLOo3utUG8dnprNBj917wPpIPQXz2uYhCLzZrvAPEZ7+LOHWMmTXeAeIz4yIvhmMhRjbx2Vor9y5hpmq1YUmY92q1BU8Y0y243EhtKOb+WoVJE+a8WgX+E2UnsMBMaBVb7lY3zGXCVGQVWq4VN8xlhQ+hT4uZbpAgfwOnmAutYkuVgDrxkybT3wpcDJwKHCECApdo9YV3tDbIIeQaybvAPV5EVqGlFEMdmASWdbuQAScAjwKPAyd5E/iwGhuS4Jcrv+tgsfUU6pKEbsQ24HKXC/LVSaTmRi9sBha63NDzwJymi4tcxtVkUix0UsTyDn0ZAp4Dvga2ayx9g6QRALfJxaiS/g/r32zQ98h7v9JnDWV7/W0A76J04VMvQkZ8FVPt3wh1+zrVIREX8DFLsaVyS8osq7D9jR6e8wdwDXCt/h72EqheUZZRk+pmZEHFSO6V2cM2Lt1iM7LlQrpeTE+NNyvm5E7ThSV7zebsEGUk+uCWEltlsQrNsyZCawfu9FyRsVcuLbFTPIPQfGkmtHZiJCGxh0pslGqOodluKnTbyE5hGjnGKOsqrWymgjk79gK5sMQ28UbyTbIp8UZiun5XlNg1kXXuR4WfPR5pB/lIiU13RLBl2KvQbZ27TiuXRx9FeqLfay7hIGwKWqGdVtWaNXpEH4I/y+pqAE+Q8+3aHgqrjAYqRzFS8aFbFqgtY7Io+hcUWrU/7gM+9Xi6vr7sayuLJfAP/pBnX+ZSglbV3NXA+30GboriC2u1VmppARPgBfzxvEsZWouVjLYHgZdVsHW6qMzohuOAfiA/a7xYPqDXJOEQuLDbxUeie/p8ayayOACOcAb6vaHI00GKW+UIraIvcoA7KFuBM2L3J2l0JzuIJyT/7uSs2P3IAuCCPsWWteL82PZnBXAmsLEHkbcA58S2O0uA07sMGchttaWx7c0aWjvYquT7z2r9r6Ai+PSvF4j8dvStdR2hdUQn7p/8rOrnIf8BrIGFEsG9lLcAAAAASUVORK5CYII="/>
        </defs>
        </svg>
        <p><strong>시</strong>간별로 <strong>추</strong>천영화</p>
      </div>
      <div class="rightside-container" @mouseover="expandRight" @mouseleave="shrinkRight">
        <svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="90" height="90" fill="url(#pattern0_141_6)"/>
        <defs>
        <pattern id="pattern0_141_6" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use xlink:href="#image0_141_6" transform="scale(0.0111111)"/>
        </pattern>
        <image id="image0_141_6" width="90" height="90" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAADuElEQVR4nO2cWahNURiAPy4is0KJTGV6MJaIkESeJBEPpsKjIlG6yoOhLg94NYuUIVOSRJnKEA9kzFBKyBDdcK/p18oS9zjnOOfsYa299//V/3zW+s7Z6/x7/f9aoCiKoiiKoiiKoihKimkGzARWAmNdDyaNNAUWAE8B+SvWuB5YmhgP3M0R/Du+A71cDzDptAf2FhD8d0xxPdAkMw54VoJkE/1cDzapLAK+lij5vOvBJpEmwLYSBYsuG5WnbYfKlPwQaBzyl516yafKlCzActcDTxKNgN0VSBagr+vBJ4maCiXfdz3wJDED+FGh6I2uB58UzGNfW6FkAWa5nkASMJnCxQCSBRjgehJJYFlAyZ9tzq0UoUvAJUNs/qz8h10BJQtwTS0Xp5/d1gwq+oyKLk6lLyaSE4dVdGG6Al9CEn1cRRdmVUiSBTinogvnzU9CFH1dRednRIiSBXilovOzNmTRAnRQ2f9yMwLRI1V0Q9oA3yIQvVRFN2RSBJIFOKGiG7IiItEfbPeSYim3ql1OTFHLfzgfoehDKvoPDyIUXQd0Utm/eBOhaAHWqehflNraFeRPsb3KjiaHlpzYoKLD2xqVImGemkFZlx20PiglhqmqV5FhHsUkWoDVZJhLMYr+Zo9hZJJyW3GDxvusrtfrYxYtwHOgBxljugPRYo/J9SFD9HYkWmzJaxgZajR/7VD2R2A+GWGPQ9Fiw4yhLSnH1TotOfECmGOfstTWDes9EC02LtkSWxy0BKYC8+LKhPZ7IFjydKXOtjLCpj+wxeb1vz+v3j5RkTLWA7FSIGptA6Y5U9OxwvmZ5WgoUA1cKXI252Mc27p3PJAq/wkj6Bawz/YLmrMyE4Dh9jjHEHtO3dQrFwKbgbNlZlajoxY91wOR4jjMlm7nqEVXJeRXLRHGVmJimgeTFUfxCegWl2jzp3Hag0mLgzD3QMVK9xgrL+JJ3HbVWbXYg8lLTFFnUz8nmCXkiAcSJIZYgmNaZSALOejL3oo5e/jWAyES0St+CzxiMPDOAzESYjyI48WkEkalKBO5Z8+8e4vZT3jpgSgJEDcCbEzFSs8i12OK53EUaE2CaAcc8ECclNG4szrJV8PNScC6/Swt1yv3Ao55IDTfducmW6ZLFRM9erk5CQwkxTS226xXHcj9bq+viLw64htjgJ05xc+o+vhqstZelo/m9le+A3gcUs3wjr3AcHzWm9uL0c1Ws6ttd9Jl2wz/MieDeWvf4C4A2+0J38l6a4KiKIqiKIqiKAql8xNSKRqpmfcoiwAAAABJRU5ErkJggg=="/>
        </defs>
        </svg>
        <p class="black-font">평일 저녁 가벼운 마무리!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const expandLeft = () => {
  const leftContainer = document.querySelector('.leftside-container')
  const rightContainer = document.querySelector('.rightside-container')
  leftContainer.style.width = '40%'
  rightContainer.style.width = '20%'
  leftContainer.style.backgroundColor = '#e5dfcc'
}

const shrinkLeft = () => {
  const leftContainer = document.querySelector('.leftside-container')
  const rightContainer = document.querySelector('.rightside-container')
  leftContainer.style.width = '30%'
  rightContainer.style.width = '30%'
  leftContainer.style.backgroundColor = 'white'
}

const expandRight = () => {
  const leftContainer = document.querySelector('.leftside-container')
  const rightContainer = document.querySelector('.rightside-container')
  leftContainer.style.width = '20%'
  rightContainer.style.width = '40%'
  rightContainer.style.backgroundColor = '#e5dfcc'
}

const shrinkRight = () => {
  const leftContainer = document.querySelector('.leftside-container')
  const rightContainer = document.querySelector('.rightside-container')
  leftContainer.style.width = '30%'
  rightContainer.style.width = '30%'
  rightContainer.style.backgroundColor = 'white'
}

const navigateToForYouView = () => {
  router.push('/foryou')
}
</script>

<style scoped>
* {
  color: white;
}
.containertoRecommend {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.toRecommend-title {
  align-self: flex-start;
  margin-left: 60px;
  margin-top: 40px;
}
.toRecommend-container {
  margin-top: 40px;
  width: 100%;
  height: 30vh;
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}
.toRecommend-container > div {
  width: 30%;
  transition: width 0.5s ease;
}
.leftside-container {
  border-top-right-radius: 100px;
  border-bottom-right-radius: 100px;
  background-color: white;
  padding-left: 30px;
}
.leftside-container > svg {
  margin-top: 60px;
}
.rightside-container {
  border-top-left-radius: 100px;
  border-bottom-left-radius: 100px;
  background-color: white;
  text-align: right;
  padding-right: 30px;
}
.rightside-container > svg {
  margin-top: 60px;
}
.linkToRecommendButton {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: none;
}
.linkToRecommendButton > svg {
  cursor: pointer;
}
.linkToRecommendButton > p {
  margin-top: 20px;
}
.linkToRecommendButton strong {
  color: #E5DFCC;
  font-weight: bold;
  font-size: 20px;
}
.black-font {
  color: black;
  margin-top: 20px;
}
</style>