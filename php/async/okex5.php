<?php

namespace ccxt\async;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use ccxt\async\abstract\okex5 as okex;

class okex5 extends okex {

    public function describe() {
        return $this->deep_extend(parent::describe(), array(
            'id' => 'okex5',
            'alias' => true,
        ));
    }
}
